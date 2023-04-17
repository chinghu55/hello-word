import awswrangler as wr
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


def lambda_handler(event, context):
    # TODO implement
    data_month = date.today() + relativedelta(months=event['data_month'])
    year = data_month.year
    month = data_month.month
    savings_plan_list_df = pd.DataFrame()

    # get db & table name from INFORMATION_SCHEMA
    query = """
        SELECT
            table_schema,
            table_name
        FROM
            COLUMNS
        WHERE
            column_name = 'savings_plan_start_time'
    """
    db_df = wr.athena.read_sql_query(
        query,
        database='INFORMATION_SCHEMA',
        ctas_approach=False
    )

    # set query string according to column(savings_plan_instance_type_family) exists or not
    for row in db_df.itertuples():
        query = f"""
            SELECT
                1
            FROM
                COLUMNS
            WHERE
                column_name = 'savings_plan_instance_type_family'
                AND table_schema = '{row.table_schema}'
                AND table_name = '{row.table_name}'
        """
        db_with_ec2sp = wr.athena.read_sql_query(
            query,
            database='INFORMATION_SCHEMA',
            ctas_approach=False
        )
        if db_with_ec2sp.empty:
            instance_type_family = "'' AS savings_plan_instance_type_family"
        else:
            instance_type_family = 'savings_plan_instance_type_family'

        # get savings plan list
        query = f"""
            SELECT DISTINCT
                bill_payer_account_id,
                line_item_usage_account_id,
                savings_plan_savings_plan_a_r_n,
                savings_plan_offering_type,
                CASE
                    WHEN savings_plan_region = 'Any' THEN ''
                    ELSE savings_plan_region
                END AS savings_plan_region,
                {instance_type_family},
                savings_plan_total_commitment_to_date,
                savings_plan_purchase_term,
                savings_plan_payment_option,
                DATE_FORMAT(from_iso8601_timestamp(savings_plan_start_time), '%Y-%m-%d %T') AS savings_plan_start_time,
                DATE_FORMAT(from_iso8601_timestamp(savings_plan_end_time), '%Y-%m-%d %T') AS savings_plan_end_time,
                product_sku
            FROM
                {row.table_name}
            WHERE
                line_item_line_item_type = 'SavingsPlanRecurringFee'
                AND year = '{year}'
                AND month = '{month}'
        """
        df = wr.athena.read_sql_query(
            query,
            database=f"{row.table_schema}",
            ctas_approach=False
        )
        savings_plan_list_df = pd.concat(
            [savings_plan_list_df, df],
            ignore_index=True
        )

    # if query result not empty, upload file to s3
    if not savings_plan_list_df.empty:
        savings_plan_list_df.sort_values(
            by=[
                'bill_payer_account_id',
                'line_item_usage_account_id',
                'savings_plan_offering_type',
                'savings_plan_start_time'
            ],
            inplace=True,
            ignore_index=False
        )
        bucket = 'terry-billing-report-for-ck'
        folder = 'dev'
        filename = f"savings_plan_list_{data_month.strftime('%Y-%m')}.xlsx"
        wr.s3.to_excel(
            savings_plan_list_df,
            f"s3://{bucket}/{folder}/{filename}",
            index=False
        )
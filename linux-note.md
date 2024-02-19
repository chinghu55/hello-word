# Linux 指令 note
sudo su [切換成 root permission]
chmod [檔案權限改變]
mkdir [創目錄]
rmkdir [刪除空目錄]

touch [目錄]/[文件名稱].[副檔名] - 建立文件

vi [編輯文件起手式]
	i [代表inset]
	:wq [編輯完存檔離開]
	/（向後搜尋）
	
chmod 400 coletest_key.pem [更改 key pair 的權限]
ssh -i "coletest_key.pem" ec2-user@ec2-52-87-223-174.compute-1.amazonaws.com
sudo vi resolv.conf 

# 要查詢某一個套件是否已經安裝, 可以配合 grep 指令, 例如想查詢包括 mysql 關鍵字的套件, 可以這樣做:
rpm -qa | grep mysql
rpm -qa | grep '應用程式名稱 ex: aws、SQL' [就是看系统有沒有装指定的應用程式]

# Command line 常用基本指令
pwd --Print Working Directory：所在位置
ls --List：資料夾下所有檔案
cd --Change Directory：切換位置(補充：cd.. 切到上層）
man --Manual：使用說明書
touch：建立檔案、更改時間
rm --Remove：刪除
mkdir --Make directory：建立資料夾
mv --Move：移動、更名
cp --Copy：複製

# Command line 其他好用指令
vim：文字編輯器(補充：wq 存檔跳出、i 插入文字、esc 普通編輯模式)
grep：抓取文字
wget：下載檔案
echo：印出文字
curl：送出 request
">"：重新導向
">>"：新增內容
"|"：把很多指令接起來

# 安裝 nginx 的指令
sudo amazon-linux-extras install nginx1 [Amazon Linux 2 所以要輸入 sudo amazon-linux-extras install nginx1 來進行安裝]
sudo systemctl start nginx [啟動 Nginx]
sudo systemctl enable nginx [設定開機後 Nginx 自動啟動]
sudo systemctl status nginx [檢查 nginx 狀態]
sudo systemctl stop nginx [關閉 nginx]

# chown 是 Linux 用來變更檔案或目錄的管理者或群組
sudo chown [newuser] [filename]  - 指定檔案 filename 的管理者改成 newuser
sudo chown :[newgroup] [filename] - 可以更改指定檔案的群組
sudo chown [newuser]:[newgroup] [filename] - 要同時修改管理員及群組，這可以這樣寫

# mv $1 $2
- $1: 舊檔案或資料夾名稱
- $2: 新的檔案或資料夾名稱
mv oldname.txt newname.txt

# 背景執行
/usr/bin/php 程式   > /dev/null 2>&1 &
*加上 & 就是背景執行
* > /dev/null 表示輸出結果不儲存 表示都到垃圾桶不輸出 (> 輸出至哪裡)

[timeout]
GET -t 0 http://domain  > /dev/null &
*-t 0 就是set_time_limit(0);的意思

# 監控
top
top -p XXXX  *XXX 表示要監控的process id
ps -ef | grep http ps -ef | grep php *可找出執行的process id(pid)
kill pid *可刪除執行緒 

# aws cli v2
要更新 cli 版本，可以參考的操作[1]，最後設定要記得到[2]將作業系統的 PATH 更新(Possible cause: The operating system PATH was not updated during installation)

[1]安裝或更新至 AWS CLI 的最新版本:
https://docs.aws.amazon.com/zh_tw/cli/latest/userguide/getting-started-install.html

[2]AWS CLI Troubleshooting:
https://docs.aws.amazon.com/zh_tw/cli/latest/userguide/cli-chap-troubleshooting.html

PATH 更新後, 回到[1]的第4步中提到的 Note 執行 --update parameter
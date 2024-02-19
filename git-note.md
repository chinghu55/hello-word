# Git 
> 參考網址:  
Day 06：Git 學習筆記:https://ithelp.ithome.com.tw/articles/10294118  
Markdown 官方教程:https://markdown.com.cn/basic-syntax/line-breaks.html  
連猴子都能懂的Git入門指南:https://backlog.com/git-tutorial/tw/intro/intro1_1.html  
紅寶石Git教學: https://gitbook.tw/


### 使用 Git 前必知：常用終端機命令列指令
| windows | mac/linux | 說明               |
| ------- | --------- | ------------------ |
| cd      | cd        | 切換目錄           |
| cd      | pwd       | 取得目前所在位置   |
| dir     | ls        | 列出目前的檔案列表 |
| mkdir   | mkdir     | 建立新的目錄       |
| 無      | touch     | 建立檔案           |
| copy    | cp        | 複製檔案           |
| move    | mv        | 移動檔案           |
| del     | rm        | 刪除檔案           |
| cls     | clear     | 清除畫面上內容     |


### 簡明Vim操作介紹
Vim 主要是使用模式的切換來進行輸入、移動游標、選取、複製及貼上等操作。在 Vim 主要常用的有幾個模式：Normal 模式以及 Insert 模式。示意圖如下：
![image](https://gitbook.tw/images/tw/command-line/vim-introduction/mode.png)  

說明如下：

- Normal 模式，又稱命令模式，在這個模式下，無法輸入文字，僅能進行複製、貼上、存檔或離開動作。
- 要開始輸入文字，需要先按下 i、a 或 o 這三個鍵其中一個進入 Insert 模式，便能開始打字。其中，i 表示 insert，a 表示 append，而 o 則是表示會新增一行並開始輸入。
- 在 Insert 模式下，按下 ESC 鍵或是 Ctrl + [ 組合鍵，可退回至 Normal 模式。
- 在 Normal 模式下，按下 :w 會進行存檔，按下 :q 會關閉這個檔案（但若未存檔會提示先存檔再離開），而 :wq 則是存檔完成後直接關閉這個檔案。 
   
Vim 的指令還非常多，但就以在 Git 會遇到的狀況來說（主要是編輯 Commit 訊息），上述這些指令應該已經足夠使用。


## Git 工作區域分為三種
Working Directory: 工作目錄，也就是在你本地電腦的資料夾
Staging Area: 暫存區，在你要上傳檔案到遠端伺服器GitHub時，Git會先將你的檔案快照暫存起來，下Commit後才會存放到Repository。暫存區會放在本地端。
Repository: 儲存庫，用來存放你提交的檔案。而儲存庫會放在遠端，也就是 GitHub。

示意圖:  
![image](https://i.imgur.com/usZr4HH.jpg)

## Commit Message組成規範
| Type      | 使用說明                   |
| --------- | -------------------------- |
| feat:     | 新增或是修改功能           |
| fix:      | 修補某個Bug                |
| docs:     | 文件類檔案                 |
| style:    | 不影響功能的樣式、格式變動 |
| refactor: | 重構、效能提升與程式碼優化 |
| perf:     | 改善效能                   |
| test:     | 增加測試功能               |
| chore:    | 非關程式碼變動的一切調整   |
| revert:   | 撤回先求的commit           |

*Commit Message 就像是寫程式要寫註解一樣，好的 Message 會節省看 Code 的時間。*

## Git 常用基本指令
- git config --global user.name "<使用者名自>"
- git config --global user.email "<電子信箱>"  

*Git的設定會被記錄在用戶的目錄首頁下的.gitconfig檔案裡。*

- git config --global alias.co checkout : 可以為Git的命令設定別名，例如checkout可以省略為co來執行
- git init--initial：告訴 Git 要做版本控制，用來初始化
- git status：查詢狀況
- git add + (檔案名稱)：將檔案加入版本控制
- git rm --cached + (檔案名稱)：將檔案移除變 untracked
- git commit：新建版本
- git commit -sm + (訊息)：新建版本且可留言
- git log：查看歷史資料(補充：+ --online：簡短歷史資料)
- git checkout：回到之前版本
- git checkout master：回到最新狀態
- git remote -v : 顯示遠端的Repository
- git fetch [遠端節點名稱] [分支名]

(多加兩個空格就可以換行)  
**git add : 加入版本控制，把檔案放入一個temp(暫時) 的資料夾**  
**git commit : 新建版本，把temp這個資料夾改名**

## Git branch (分支)常用基本指令
- git branch + (名稱): 建立 branch
- git branch -v : 查看有哪些 branch  
- git branch -d : 刪除 branch  
- git merge : 合併 branch (marge 可能會造成衝突 (conflick)，此時需要手動解決)


**git checkout -b "branch-name" : 建立新的branch並切換過去**


## AWS CodeCommit

### 本機 ssh pubilc keys for aws codecommit
首先在本機產出key pair

在本機cmd下以下操作:  
>cd ~/.ssh/  
ssh-keygen  
![image](keygen.png)  

產出public key後就可以進到檔案裡面將key複製貼到IAM user的SSH public keys for AWS CodeCommit上。  
接著需要在 ssh/ 新增 config 檔案，範例如下圖:  
![image](codecommit_ssh01.png)  
![image](codecommit_ssh02.png)

最後再CodeCommit上Clone SSH並下在cmd:  
git clone ssh://Your-SSH-Key-ID@git-codecommit.us-east-1.amazonaws.com/v1/repos/coletest

*加上 'Your-SSH-Key-ID' 目前認為我是 win11 + ubuntu 雙系統，參考文件內就針對 windows 的做參考*  
*如果存 linux 的話，從文件表示是不需要輸入 'Your-SSH-Key-ID'*

參考網址:
https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-windows.html

### HTTPS Git credentials for AWS CodeCommitd
git remote add aws "Clone HTTPS"  
![image](codecommit_https.png)  
![image](codecommit_https_01.png)  

```git
git init  
git status  
git add .  
git commit -m "輸入一些描述"  
git push ssh://Your-SSH-Key-ID@git-codecommit.us-east-1.amazonaws.com/v1/repos/"Your-repos-name"
```


# 用 Git 東西與 gitlab 溝通
# 要用 WSL 用 PS 會報錯
# Tutorial: Make your first Git commit
Enter git clone and paste the URL:
$ git clone Clone-with-SSH

Go to the directory:
$ cd Clone-directory

By default, you’ve cloned the default branch for the repository. Usually this branch is main. To be sure, get the name of the default branch:
$ git branch

Create a new branch called example-tutorial-branch:
$ git checkout -b example-tutorial-branch

Edit README.md file and add this text and Save the file:
Hello world! I'm using Git!

Git keeps track of changed files. To confirm which files have changed, get the status:
$ git status

Add the README.md file to the staging area. The staging area is where you put files before you commit them.
$ git add README.md

Confirm the file is staged:
$ git status

現在提交暫存文件，並包含一條描述您所做更改的消息。
$ git commit -m "I added text to the README file"

The change has been committed to your branch, but your branch and its commits are still only available on your computer. No one else has access to them yet. Push your branch to GitLab:
$ git push origin example-tutorial-branch

Now you’re ready to merge the changes from your example-tutorial-branch branch to the default branch (main).
Check out the default branch for your repository.
$ git checkout main

Merge your branch into the default branch.
$ git merge example-tutorial-branch

Push the changes
$ git push

# DONE !


# Add a file to a repository
git init
git remote add origin git@43.206.255.40:terraform/gitlab.git
git remote -v (確認有 remote 成功)
git fetch origin --all (將遠端的內容拉到local)

Choose a Git branch to work in. You can either:
- **Create a new branch** to add your file into. Don’t submit changes directly to the default branch of your repository unless your project is very small and you’re the only person working on it.

- **Switch to an existing branch.**

git branch
git checkout test
git status
git add .
git commit -m "upload file"
git push origin test

git checkout main

#可以使用這個命令來取消commit
git reset --soft HEAD^ *HEAD^是上一個版本的意思，如果要回退到前n個，那麼就是HEAD~n*

# chinghu55 github
git@github.com:chinghu55/terraform.git

# 要ignore請查看以下網址
https://gitbook.tw/chapters/using-git/ignore

# git reset 命令
https://www.runoob.com/git/git-reset.html
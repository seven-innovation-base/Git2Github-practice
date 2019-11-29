### git的一些基本信息

#### 工作区

&nbsp;&nbsp;&nbsp;工作区指的就是你看到的这个文件夹，包含.git这个隐藏文件的文件夹

#### 暂存区

&nbsp;&nbsp;&nbsp;暂存区一般存放在你git目录下的index文件中，你一般是不会看到的，用于临时存放你的改动

#### 版本库

&nbsp;&nbsp;&nbsp;版本库就是你安全存放数据的位置，就是在你最后提交到的地方，也可以说是你之后存放文件的地方

#### 关于它们的联系(我是这么理解的)

&nbsp;&nbsp;&nbsp;当你对你的文件夹进行操作，也就是对工作区进行操作，比如修改文件或者是删除文件，这些操作是在你的工作区里进行的，其实还没有对你的版本库进行到修改，所以你要你要线把这些改动操作添加的暂存区里，在暂存区里就会有这些没提交到版本库里的改动操作，你可以在暂存区里选择你要提交的改动操作，提交到版本库之后，版本库就会进行这些改动的操作，最后达到你想要的状态

### 本地库操作

#### git的添加

```java
//将操作提交的暂存区
	git add file
```

#### git提交

```Java
//将暂存区中没提交的操作提交到本地版本库
	git commit file
//因为git每次提交都需要写日志来清楚知道修改了什么，所以可以这么写
	git commit -m"message" 
//还能怎么写,-a表示执行修改或删除的操作都提交到本地库，可以不用add操作
    git commit -a -m"message"
```

#### git状态查看

```java
//查看库中有无修改操作，即有无操作可以add或commit
	git status file
```

#### 查看历史记录

```java
//这些操作都是查看历史版本的，只是显示的方式不同
git log 
git log --pretty=oneline
git log --oneline
git reflog 			//这个方式比较好看出索引和易于前进后退
```

#### 前进后退

```Java
// 基于索引操作
	git reset --hard "索引值"
// 用^来操作
    git reset --hard Head^^		//该操作只能后退，一个^后退一个版本
//用~来操作       
    git reset --hard Head~n		//这样表示后退n个版本    
```

#### reset三个参数的对比

##### soft
- 仅仅时在本地库移动HEAD指针

##### mixed
- 在本地库移动HEAD指针

- 重置暂存区

##### hard

- 在本地库移动HEAD指针
- 重置暂存区
- 重置工作区

#### 从本地库中删除文件

```Java
//用rm命令把文件从工作区删除
	rm file
//此时用status命令可以发现该操作可以添加到暂存区
    git add file
//然后把该操作提交到本地版本库就可以从本地库中删除该文件
     git commit -m"delete a file"
```

#### 比较文件差异

```Java
//将工作区中的文件和暂存区进行比较
		git diff file
//将工作区中的文件和本地库历史记录比较，不带文件名时多个文件比较
        git diff [历史版本] file      
```

### 分支操作

#### 查看分支情况

```Java
	git branch
    git branch -v 
```

#### 新建分支

```Java
	git branch branch_name
```

#### 切换分支

```java
	git checkout branch_name
```

#### 合并分支

```java 
//切换到被合并的分支上，然后执行merge命令
	git merge branch_name		
```

### 关于远程仓库的操作

#### 关于远程仓库的地址

```Java
//查看现在库里保存的远程仓库的地址
git remote -v
//设置远程仓库的地址，也可以理解为为origin创建一个别名
git remote add origin (加上远程仓库的地址，就比如https)
```

#### 本地库的推送

```Java
git push origin master
//master可以改为其他分支，必须指定
```

####  克隆

```Java
git clone (加上远程库的地址)
//克隆会帮你初始好本地库，并帮你把远程库下载到本地，还可以为你的origin创建好别名
```

#### 拉取

```java
//pull=fetch+merge
//抓取,该操作只是把远程仓库的东西下载下来，并没有修改你本地的文件
	git fetch origin master 
//这时你可以切换到origin/master这个分支上查看变化
    git checkout origin/master
//然后通过两个分支的合并就可以变成远程仓库的样子
    git merge origin/master
//当然直接执行pull也可以
	git pull origin master
```
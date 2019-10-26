# Git2Github-practice
## 大家的git练习仓库
**请大家遵守以下练习规则：**
- 1. 新加入的同学请`clone`克隆master分支。
- 2. 在master分支的基础上创建自己的分支，在这个分支里面自由练习。
- 3. 禁止强推`git push -f`
- 4. 请注意分支命名规则，请用自己的昵称加分支名称命名，如CkaiGrac-PYMO。禁止出现test1、dsafqwe等不规范命名。

### 开始练习
**克隆本项目：**
```shell
git clone https://github.com/seven-innovation-base/Git2Github-practice.git
```
**查看并创建自己的分支**
```shell
# 查看当前分支，默认为master分支，按q退出
git branch

# 创建自己的分支
git branch CkaiGrac-PYMO

# 切换到自己的分支
git checkout CkaiGrac-PYMO

# 再次查看当前分支
git branch
```

**完成自己的练习**
在自己的分支上练完后想要提交这一次修改到Github上：
- 使用git add命令，add后面可以添加单个修改后的文件或者是一个文件夹中所有修改后的文件到本地缓存中。

- 然后使用git commit命令对添加到缓存中的文件添加修改说明。

```shell
# 一次性添加所有修改到缓存中，仅适合少量修改，‘.’表示当前路径
# git add . 

git add src/main.java
git commit -m "添加main.java文件"

git add src/activity.java
git commit -m "新增activity.java文件"

# 一段时间后，修改了main.java的内容
git add src/main.java
git commit -m "新增xxx函数"
```

**把这次的修改提交到Github上**
```shell
git push origin CkaiGrac-PYMO
# 命令为git push origin your-branch
```

# 大家的Git练习仓库

## 目录

- [前言](#前言)
- [新人须知](致大一/)
- [分支练习~~需完善](#分支练习)
- [协作之道 pull request~~未完成](#协作之道pr)
- [深入学习](#深入学习)

## 前言

**须知**：本仓库主要用于练习Git的使用，提供大家一个展示练习成果的平台。

如果你的 organization 角色是 member，那么我们推荐你练习使用 pull request（pr）。

如果你的角色[（role）](https://github.com/orgs/seven-innovation-base/people)是 owner，我们仍然推荐你练习使用pull request（pr），不要直接在当前repository创建分支，先[fork](https://github.com/seven-innovation-base/Git2Github-practice/fork)这个repository，然后再创建个分支做改动后向本仓库提交pr展示你的练习成果。

了解Fork Projects🍳[{GitHub Guides-Forking Projects}](https://guides.github.com/activities/forking/)

**如果对Git没一丁点认知，请先阅读😘[新人须知](致大一/)**

## 分支练习

**请大家遵守以下练习规则：**

- 1. 新加入的同学请 `clone`克隆master分支。
- 2. 在master分支的基础上创建自己的分支，在这个分支里面自由练习。
- 3. 禁止强推 `git push -f`
- 4. 请注意分支命名规则，请用自己的昵称加分支名称命名，如CkaiGrac-PYMO。禁止出现test1、dsafqwe等不规范命名。

**克隆本项目：**

```shell
git clone https://github.com/seven-innovation-base/Git2Github-practice.git
```

**查看并创建自己的分支**

```shell
# 查看当前分支，默认为master分支，按q退出
git branch

# 根据当前所在分支创建自己的分支
git branch CkaiGrac-PYMO

# 切换到自己的分支
git checkout CkaiGrac-PYMO

# 再次查看当前分支
git branch
```

**完成自己的练习**

在自己的分支上练完后想要提交这一次修改到GitHub上：

- 使用 `git add` 命令，add后面可以添加单个修改后的文件或者是一个文件夹中所有修改后的文件到本地缓存中。

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

## 协作之道pr

## 深入学习

- 实验楼的这门以战代学的课程不错，有在线模拟环境是它的亮点👉👉[Git与Github入门实践](https://www.shiyanlou.com/courses/1035)

- 学长学姐告诉你，查文档学习更快，以实际应用场景为驱动，学得更快更有效率（逃~~~，👉👉[Git Documentation](https://git-scm.com/doc)

- [GitHub Flow](https://guides.github.com/introduction/flow/)

- [断点续传式git clone（伪）-逐步clone](https://blog.csdn.net/zerooffdate/article/details/79348925)
# 大家的Git练习仓库
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## 目录

- [大家的Git练习仓库](#大家的git练习仓库)
  - [目录](#目录)
  - [前言](#前言)
  - [新人需知](致大一/)
  - [分支练习](#分支练习)
  - [协作之道pr](#协作之道pr)
  - [深入学习](#深入学习)
  - [已参与娱乐的小伙伴 ✨](#已参与娱乐的小伙伴-)

## 前言

**须知**：本仓库主要用于练习 Git 的使用，提供大家一个展示练习成果的平台。

如果你的 organization 角色是 member，那么我们推荐你练习使用 pull request（pr）。

如果你的角色[（role）](https://github.com/orgs/seven-innovation-base/people)是 owner，我们仍然推荐你练习使用pull request（pr），不要直接在当前 repository（仓库） 创建分支，先[fork](https://github.com/seven-innovation-base/Git2Github-practice/fork)这个 repository，然后再创建个分支做改动后向本仓库提交pr展示你的练习成果。

了解 Fork Projects🍳[{GitHub Guides-Forking Projects}](https://guides.github.com/activities/forking/)

**如果对Git没一丁点认知，请先阅读😘[新人须知](致大一/)**

## 分支练习

**请大家遵守以下练习规则：**

- 1. 新加入的同学请 `clone`克隆 main 分支。
- 2. 在 main （主）分支的基础上创建自己的分支，在这个分支里面自由练习。
- 3. 禁止强推 `git push -f`
- 4. 请注意分支命名规则，请用自己的昵称加分支名称命名，如 CkaiGrac-PYMO。禁止出现 test1、dsafqwe 等不规范命名。

**克隆本项目：**

```shell
git clone -b main https://github.com/seven-innovation-base/Git2Github-practice.git --single-branch
```

**查看并创建自己的分支**

```shell
# 查看当前分支，默认为 main 分支，按 q 退出
git branch

# 根据当前所在分支创建自己的分支
git branch CkaiGrac-PYMO

# 切换到自己的分支
git checkout CkaiGrac-PYMO

# 再次查看当前分支
git branch
```

**完成自己的练习**

在自己的分支上练完后想要提交这一次修改到 GitHub 上：

- 使用 `git add` 命令，add 后面可以添加单个修改后的文件或者是一个文件夹中所有修改后的文件到本地缓存中。

- 然后使用 git commit 命令对添加到缓存中的文件添加修改说明。

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

好了，到了这里，前面的分支学习将真正有“大作为”。在多人合作时，我们可能会有这样一个情景，你 clone 到本地的版本库与远程的版本库历史（commit log）不一致（有可能你 clone 项目后，有人也 clone 了，并对他的修改进行了提交），导致你不能提交「当然，你强制提交也行，但是这并不推荐」。这如何解决呢？

在多人合作时，我们有这样的一个分支维护习惯（也许还有更好的）：

- 主分支保持 stable；
- clone 项目后，不在主分支（main）进行修改，而是**新建立一个分支进行修改**；
- 主分支用于同步远程变更，同步完成后在把远程新的变更 merge 到你工作的分支（branch）；

那么，如何操作，以下是一种基于「 GitHub 演示」良好的实践：

我们晓得，一般情况下，如果你不是项目的核心维护者，你是没有权限直接提交修改到项目的仓库的，这时你就会用到 GitHub 的 fork 操作。以下以[基地的文档项目](https://github.com/seven-innovation-base/SphinxDOC)为例子。

```bash
# fork 之后你会进行 clone
git clone https://github.com/your_username/SphinxDOC
```

在你 push 变更到你fork后的仓库时，**你需要注意**：fork 后仓库的历史变更不会和真正的项目仓库历史变更保持同步，在 push 之前，我们会有以下这两波操作解决：

**方法一**：

- 1、添加源仓库为你 fork 后仓库的远程上游

```bash
git remote add upstream https://github.com/seven-innovation-base/SphinxDOC.git
# 或者
git remote add upstream git@github.com:seven-innovation-base/SphinxDOC.git
```

- 2、切换回主分支（main），同步远程上游的变更，并将变更合并到主分支

```bash
git checkout main
git fetch upstream
# 你也阔以看看当前主分支和 upstream 的有什么不同
# git diff upstream/main
git merge upstream/main
```

- 把变更 merge 到你工作的分支，然后 git commit、git push，最后再到 GitHub 提交 pull request

![github pr.jpg](https://i.loli.net/2020/05/02/KhvHpjMDfT34yVs.png)


**方法二：**

- 1、 自 2021 年 5 月 7 日，GitHub 已经支持一键同步和一键 pull request，在自己 fork 之后的仓库里，``Code`` 下有功能 ``fetch and merge`` （如  下图），能够使得你在网页端的仓库与源仓库同步。

[![g3lJ7n.png](https://z3.ax1x.com/2021/05/07/g3lJ7n.png)](https://imgtu.com/i/g3lJ7n)


- 2、 如果你本地工作仓库也需要更新，那么直接 ``git fetch`` 、``git merge`` 即可将本地工作仓库与远程仓库内容同步。

- 3、  如果你想将自己的修改好的分支推到源仓库上你还需要再（如 下图）





到这里，你应该明白了，应该深入了解波 `git fetch` 和 `git merge` 的相关实践


## 深入学习

- 这里可能会有你学习和使用 Git 的时候遇到的各种问题 -> [Git 飞行指南](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)

- 实验楼的这门以战代学的课程不错，有在线模拟环境是它的亮点👉👉[Git与Github入门实践](https://www.shiyanlou.com/courses/1035)

- 学长学姐告诉你，查文档学习更快，以实际应用场景为驱动，学得更快更有效率（逃~~~，👉👉[Git Documentation](https://git-scm.com/doc)

- Git 工作流：[GitHub Flow](https://guides.github.com/introduction/flow/)

- Git 处理大型仓库：[Git 如何处理大仓库](https://www.oschina.net/translate/how-to-handle-big-repositories-with-git)

- 应对大仓库的 clone 太慢的问题：[断点续传式git clone（伪）-逐步clone](https://blog.csdn.net/zerooffdate/article/details/79348925)

## 已参与娱乐的小伙伴 ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://zy68.top"><img src="https://avatars1.githubusercontent.com/u/53072382?v=4?s=100" width="100px;" alt=""/><br /><sub><b>sustart</b></sub></a><br /><a href="https://github.com/seven-innovation-base/Git2Github-practice/commits?author=MrGo123" title="Documentation">📖</a></td>
    <td align="center"><a href="https://redhat123456.github.io/"><img src="https://avatars.githubusercontent.com/u/104449?v=4?s=100" width="100px;" alt=""/><br /><sub><b>redhat123456</b></sub></a><br /><a href="https://github.com/seven-innovation-base/Git2Github-practice/commits?author=redhat123456" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Tanger"><img src="https://avatars.githubusercontent.com/u/57751257?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tanger</b></sub></a><br /><a href="https://github.com/seven-innovation-base/Git2Github-practice/commits?author=Tanger" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

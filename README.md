# 大家的Git练习仓库
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## 目录

- [前言](#前言)
- [新人须知](致大一/)
- [分支练习~~需完善](#分支练习)
- [协作之道 pull request~~需完善](#协作之道pr)
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

好了，到了这里，前面的分支学习将真正有“大作为”。在多人合作时，我们可能会有这样一个情景，你 clone 到本地的版本库与远程的版本库历史不一致（有可能你 clone 项目后，有人也 clone 了，并对他的修改进行了提交），导致你不能提交「当然，你强制提交也行，但是这并不推荐」。这如何解决呢？

在多人合作时，我们有这样的一个分支维护习惯（也许还有更好的）：

- 主分支保持 stable；
- clone 项目后，不在主分支（master）进行修改，而是**新建立一个分支进行修改**；
- 主分支用于同步远程变更，同步完成后在把远程新的变更 merge 到你工作的分支（branch）；

那么，如何操作，以下是一种基于「 GitHub 演示」良好的实践：

我们晓得，一般情况下，如果你不是项目的核心维护者，你是没有权限直接提交修改到项目的仓库的，这时你就会用到 GitHub 的 fork 操作。以下以[基地的文档项目](https://github.com/seven-innovation-base/SphinxDOC)为例子。

```bash
# fork 之后你会进行 clone
git clone https://github.com/your_username/SphinxDOC
```

在你 push 变更到你fork后的仓库时，**你需要注意**：fork 后仓库的历史变更不会和真正的项目仓库历史变更保持同步，在 push 之前，我们会有以下这波操作解决：

- 1、添加源仓库为你 fork 后长裤的远程上游

```bash
git remote add upstream https://github.com/seven-innovation-base/SphinxDOC.git
# 或者
git remote add upstream git@github.com:seven-innovation-base/SphinxDOC.git
```

- 2、切换回主分支（master），同步远程上游的变更，并将变更合并到主分支

```bash
git checkout master
git fetch upstream
# 你也阔以看看当前主分支和 upstream 的有什么不同
# git diff upstream/master
git merge upstream/master
```

- 把变更 merge 到你工作的分支，然后 commit、push，然后再到 GitHub 提交 pull request

![github pr.jpg](https://i.loli.net/2020/05/02/KhvHpjMDfT34yVs.png)

## 深入学习

- 实验楼的这门以战代学的课程不错，有在线模拟环境是它的亮点👉👉[Git与Github入门实践](https://www.shiyanlou.com/courses/1035)

- 学长学姐告诉你，查文档学习更快，以实际应用场景为驱动，学得更快更有效率（逃~~~，👉👉[Git Documentation](https://git-scm.com/doc)

- [GitHub Flow](https://guides.github.com/introduction/flow/)

- [断点续传式git clone（伪）-逐步clone](https://blog.csdn.net/zerooffdate/article/details/79348925)
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://zy68.top"><img src="https://avatars1.githubusercontent.com/u/53072382?v=4" width="100px;" alt=""/><br /><sub><b>yizhuang</b></sub></a><br /><a href="https://github.com/seven-innovation-base/Git2Github-practice/commits?author=MrGo123" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
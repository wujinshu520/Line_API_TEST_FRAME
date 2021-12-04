# encoding: utf-8
# @author: wujinshu
# @file: 1.py
# @time:2021/11/27 18:43
# @desc:
'''
git --version

git config --global user.name "wujinshu"
git config --global user.email "1964855301@qq.com"

ssh-keygen -t rsa -C "1964855301@qq.com"


SHA256:KXHEzVr2G0XZlrtGXwcQlNdMudqew76bXbMgXlhSWCQ 1964855301@qq.com

创建空的文件夹--wujinshu
进入到空的目录下：输入git init
vi test_01.py
git add test_01.py
git status
git commit -m "第一次提交"
git log
git log --pretty=oneline   查看提交的日志

git reset --hard HEAD^^  回退

git reflog 回退的日志

git reset --hard 当前版本号，恢复到当前未修改的版本

git checkout -- test_01.py

git rm test_02.py 删除文件

撤销删除


修改最后一次提交操作：
版本刚一提交（git commit）到仓库，发现注释写错或少提交了部分文件，
此时需要修正这次提交的内容，把这样的操作称为修改最后一次提交操作

操作如下：
1、手动新增一个test04.py文件，内容为：
2、使用 git add * 、 git commit -名"新增test05.py代码"进行提交到版本库
3、使用命令 git commit --amend -m "新增test04.py代码"，把最后一次提交的注释进行修改，--amend 选项的commit命令
（即 git commit --amend） git会"更正"最近的一次提交
4、再次新增一个文件test05.py文件，内容为：
5、使用git add * 命令添加到服务区
6、使用命令git commit --amend -m "新增test04.py\test05.py代码"把test05.py也置入最后一次提交的版本中
备注：过程中可以使用git log 查看日志


git管理分之：
git branch  ：查看当前分之情况
git branch dev   ：创建一个dev的新分之
git checkout 分之   ：切换到dev分之
备注：步骤2，3可以通过命令git checkout -b dev 完成相同的操作

分之合并时的冲突
1、使用命令git checkout -b dev 创建并切换dev
2、对new02.py文件进行修改，添加一行内容：XXXXX并提交到版本库
3、使用命令git checkout master
4、对new02.py文件进行修改：添加一行内容：XXXXX并提交到版本库
    上面这种情况，git无法执行"快速合并"，只能试图把格子的修改合并起来，
    但这种合并就可能会有冲突
    冲突原因：master分之和dec分之各自部分都分别有新的提交，并且编译了同一个文件


代码删除：git rm
代码文件重名： git mv

合并分之：1、git checkout master  2、git merge


git 使用详解
 1、确认是否存在：～/.ssh 目录，目录下是否存在id_rsa 和 id_rsa.pub 两个文件
 2、id_rsa 是私钥		id_rsa.pub 是公钥

GitHub + pycharm 整合=======》 几乎任何的IDE

pycharm 相关配置
pycharm 配置本地新安装的git.exe  ../.. git


测试开发组长操作流程：
1、编写好一套能用的接口测试框架
2、上传到github仓库
3、设置团队协作成员

组员操作：
1、通过邮件同意团队操作的申请
2、克隆代码到本地
3、依据公司的代码提交规范进行提交


第一步： 把该项目转化成GitHub仓库
1.1 在本地文件使用： git init

第二步： 先设置忽略的文件及文件夹

第三步：



'''

print('new01')



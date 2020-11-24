# git 忽略本地已存在文件的修改
# 将文件修改忽略
git update-index --assume-unchanged _config.yml
git update-index --assume-unchanged Gemfile.lock
git update-index --assume-unchanged .gitmodules

# 添加文件try.py
#然后git add . 将文件加入git库 
#git commit -m "add file try.py" 备注
#git push 上传
#
#修改文件之后
#git add.
#git commit -m "修改文件部分内容"
#git push

# 关机之后 重启 发现git 错误 报错如下：
# git commit -m "try again"的时候，出现 git push   打印 please tell me who you are
#这时候需要正确配置 git config  user.email "wangzhuilang@hellowang" 
#和 git config  user.name "wangzhuilang" 否则失败慧， 这从wangzhuilang@hellowang mingw64 /c/githello(master)猜出来的
#git config   设置错误会出现如下错误 git could not lock config file permission denie
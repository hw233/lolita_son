#!/bin/bash

echo "batch copy..."

save_dir="/home/svn_code/server_code/app/config"   #保存的目录
#mkdir ${save_dir}               #新建保存目录文件夹

for file in *.py;             #批量复制“.icns”格式的文件
do 
   echo ${file}
   cp ${file} ${save_dir} 
done
#!/bin/bash

echo "batch copy..."

save_dir="/home/svn_code/server_code/app/config"   #�����Ŀ¼
#mkdir ${save_dir}               #�½�����Ŀ¼�ļ���

for file in *.py;             #�������ơ�.icns����ʽ���ļ�
do 
   echo ${file}
   cp ${file} ${save_dir} 
done
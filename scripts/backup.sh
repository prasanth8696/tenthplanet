#!/bin/bash

server="dev044@192.168.0.9"
#dest_server="192.168.0.56"
backup_date=$(date +%b-%d-%y)

file_name=$backup_date.tenthplanet.tar.gz
echo $file_name


read -p "enter path to backup files " backup_paths

for path in $backup_paths 
do
	ssh  $server "tar -Pczf $file_name $path"
	if [ $? -eq 0 ]; then
		echo "file successfully backuped"
	else
		echo "backup failed"
		continue
	fi

	scp $server:$HOME/$file_name .

	if [ $? -eq 0 ];then
		echo "file transferred"
	else 
		echo "file transfer failed"
		continue
	fi

done


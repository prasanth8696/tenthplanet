#!/bin/bash

if [[ -z $1 ]];
then
	read -p "Enter USERNAME: " targetUser
else
	targetUser=$1
fi
server="4.206.132.16"

users=$(ssh shan@${server} "cat /etc/passwd | awk -F ':' '{print \$1}'")

for user in $users
do
	if [[ $user == $targetUser ]];
	then
		echo "${targetUser} Found in the ${server}"
		exit
	fi
done

echo "${targetUser} Not Found in the ${server}"
	

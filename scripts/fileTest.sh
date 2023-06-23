#!/bin/bash

file="./hello.txt"



if [ -r $file ]; then
	echo "File have read Access"
else
	echo "No read Access"
fi

if [ -w $file ]; then
	echo "File have write acess"
else
	echo "No write Access"
fi

if [ -x $file ]; then
	echo "File have ex access"
else
	echo "No Exe Access"

fi

if [ -s $file ]; then
	echo "File is not empty"
else
	echo "File is empty"
fi

if [ -d $file ]; then
	echo " is a directory"
else
	echo "Is not a directory"
fi

if [ -e $file ]; then
	echo "File is exists"
else
	echo "File is doesn't exist"
fi



echo "----------End Of Script-----------"

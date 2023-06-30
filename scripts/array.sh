#!/bin/bash

arr=('shan' 'jarvis' 2 3 4 5 5)

#print all elements
echo ${arr[@]}
echo ${arr[*]}

echo ${arr[@]:0}
echo ${arr[*]:0}

#print first elemet
echo ""
echo ${arr}

echo ${arr[0]}

#size of the array

echo ${#arr[@]}
echo ${#arr[*]}
 

#size of the particular element

echo ${#arr[0]}
echo ${#arr[1]}


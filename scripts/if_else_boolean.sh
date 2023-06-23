read -p "enter var1 " var1

read -p "enter var2 " var2

read -p "enter var3 " var3  


#Boolean operators

if [ $var1 -gt $var2 -a $var1 -gt $var3 ]; then
	echo "$var1 is largest number"
elif [ $var2 -gt $var1 -a $var2 -gt $var3 ] ; then 
	echo "$var2 is largest number"

else
	echo "$var3 is largest number"

fi


#echo "-----------------------------------"
#OR OPERATORS





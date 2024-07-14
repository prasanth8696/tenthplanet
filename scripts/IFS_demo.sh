
names="ayyappan,shan,master"


IFS=","  read -r -a new_names_arr <<< $names

echo ${new_names_arr[0]}
for na in ${new_names_arr[@]}
do
	echo $na
done

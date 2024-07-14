#Variable Declaration

PACKAGE_NAME=""
PACKAGE_VERSION=""
DOWNLOAD_URL=""
BASE_PATH=""
SAVE_PATH="$BASH_PATH/$PACKAGE_NAME-$PACKAGE_VERSION"
FILE_HASH=""
PACKAGE_NAME=""


checkFileHash() {

	



}

downloadFile() {

	if [ $3 -eq 1 ];then
		echo "download is intrupted"
		echo "tring to resume the dowload"
		wget -c $DOWNLOAD_URL $SAVE_PATH
	else
		echo "downloading..."
		wget  $DOWNLOAD_URL $SAVE_PATH

	fi

	

}


if ![ -e $SAVE_PATH ];then
	echo "$SAVE_PATH not exists"
	mkdir -p $SAVE_PATH 
else
	echo "$SAVE_PATH Exists"
	checkFileHash 

fi






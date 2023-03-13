import os

files_dict = {}
def findFiles(keyword,curDir) :
   for dirpath,dirname,filenames in os.walk(curDir):
      for file in filenames :
          if (file.find(keyword) >= 0) :
              print(file)
              files_dict[file] = os.path.join(dirpath,file)
      for name in dirname :
        findFiles(keyword,os.path.join(dirpath,name))
   return files_dict


print(findFiles('prac','/home/dev044'))

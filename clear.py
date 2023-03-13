import os
import sys
from pprint import pprint

help = '''
  -k keyword  
  -p path
  -c clear method
  -f find method
  -e extension

'''

def deleteFiles(extension) :
   count = 0
   for file in os.listdir() :
     ext = os.path.splitext(file)[1]
     if ext == extension :
        os.remove(file)
        count += 1


   print(f'{count} {extension} files deleted sucessfully in {os.getcwd()}')

files_dict = {}
def findFiles(keyword,curDir) :
   for dirpath,dirname,filenames in os.walk(curDir):
      for file in filenames :
          if (file.find(keyword) >= 0) :
              if len(files_dict) > 10 :
                  return files_dict
              files_dict[file] = os.path.join(dirpath,file)
      for name in dirname :
        findFiles(keyword,os.path.join(dirpath,name))
   return files_dict

def clearFile() :
  try :
    args = list(sys.argv)

    #find user path
    if ( '-p' in args) :
       index = args.index('-p')
       curPath = args[index+1]
    else :
       curPath = os.path.join(os.environ.get('HOME'),'Downloads')

    if (os.path.exists(curPath)) :
       os.chdir(curPath)
    else :
       raise FileNotFoundError

    #find user extension

    if ('-e' in args) :
       index = args.index('-e')
       extension = f'.{args[index + 1]}'
    else :
       extension = '.pdf'

    deleteFiles(extension)

  except FileNotFoundError :
    print('Invalid path...')

  except :
    print("something went wrong")
    exit()

def findFile() :
  try :
    args = list(sys.argv)

    #find user path
    if ( '-p' in args) :
       index = args.index('-p')
       curPath = args[index+1]
    else :
       curPath = os.environ.get('HOME')

    if not(os.path.exists(curPath)) :
       raise FileNotFoundError

    if ('-k' in args) :
       index = args.index('-k')
       keyword = args[index + 1]
    else :
      raise ValueError

    List = findFiles(keyword,curPath)
    pprint(List)

  except FileNotFoundError :
    print('Invalid path...') 
 
  except ValueError :
    print('please provide keyword to search...')

 # except :
#    print('something went wrong...')



param_list = list(sys.argv)


if ('-c' in param_list) :
   clearFile()
elif('-f' in param_list) :
   findFile()
else :
   print('operation not found use -f for find or -c clear the files')
   print(help)

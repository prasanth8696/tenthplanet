import os
import sys

def deleteFiles(extension) :
   count = 0
   for file in os.listdir() :
     ext = os.path.splitext(file)[1]
     if ext == extension :
        os.remove(file)
        count += 1


   print(f'{count} {extension} files deleted sucessfully in {os.getcwd()}')


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

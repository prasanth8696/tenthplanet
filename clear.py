import os
import sys
count = 0
#change the directory into downloads
try :
  if sys.argv[1] :
     os.chdir(sys.argv[1])
except  IndexError :
     os.chdir(os.path.join(os.environ['HOME'],'Downloads'))
except :
   print("invalid path")
   exit()

try :
  if sys.argv[2] :
     extension = f'.{sys.argv[2]}'
except IndexError :
     extension = ".pdf"

except :
  print("something went wrong")
  exit()

for file in os.listdir() :
    ext = os.path.splitext(file)[1]
    if ext == extension :
        os.remove(file)
        count += 1


print(f'{count} files deleted sucessfully')

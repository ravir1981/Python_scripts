import glob
import os
import time

currentTime = time.strftime("%m/%d/%Y-%H:%M:%S")
print(currentTime)

cwd = os.getcwd()
print(cwd)

getHome = os.path.normpath(os.getcwd() + os.sep + os.pardir)
print(getHome)

myfiles = glob.glob(f"{getHome}/Files/*.txt")
print(myfiles)

for file in myfiles:
    print("File is -> ", file)
    with open(file, 'r') as readfile:
        print(readfile.read())



import os

dir_path = "/Users/ravindranradhakrishnan/Documents/Python/Udemy/pythonProject"

files = os.listdir(dir_path)
print("Files are -> ", files)

"""
for root, dir, files in os.walk(dir_path):
    for file in files:
        print("Files -> ", os.path.join(root,file))
"""
file = "/Users/ravindranradhakrishnan/Documents/Python/Udemy/pythonProject/create_my_mood.py"

directory = os.path.dirname(file)
print("File's folder is -> ", directory)

cwd = os.getcwd()
print("CWD is :", cwd)
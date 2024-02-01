import csv
import glob
import os.path
import shutil

getHome = os.path.normpath(os.getcwd() + os.sep + os.pardir)
myfiles = glob.glob(f"{getHome}/Files/*.csv")
print(myfiles)
#shutil.make_archive("csv_output", "zip", "../Files")

for file in myfiles:
    print(file)
    if "climate.csv" in file:
        with open(file, 'r') as csvfile:
            data = list(csv.reader(csvfile))

print(data)
city = input("Enter the city to check weather:")

for record in data[1:]:
    if record[0] == city:
        print(f"{record[0]} weather is {record[1]}")

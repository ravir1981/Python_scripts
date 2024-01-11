string = '''Have a good Day'''
print(type(string))

### both will yield same result
print(string[-1])
print(string[14])
print("Print the last word: ", string[12:])
"""
# Finding index
print(string.index('Day'))

mylist = ['a', 'b', 'e']
print(mylist[1])
mylist[1] = 'B'
print(mylist)
targetIndex = mylist.index('e')
mylist[targetIndex] = "egg"
print("After change value in List: ", mylist)


seconds = [1.23, 1.45, 1.02,4.10,5,10]
current = 1.11
seconds.append(current)
print(seconds)
for index,second in enumerate(seconds):
    print(f'{index}-{second}')

filenames = ["1.Raw Data.txt", "2.Human organs.txt", "3.The world.txt"]
print(filenames)

for file in filenames:
    file = file.replace('.', '-', 1)
    print(file)

print("Files ", filenames)

ranking = ['John', 'Sen', 'Lisa']
name = input("Enter the name to get the index:")
index_value = ranking.index(name)
print("Index of ", name, " is ", index_value)


waiting = ['sen','ben','ban','dan']
waiting.sort()
print(waiting)
for index, item in enumerate(waiting):
    print(f"{index}.{item.capitalize()}")
"""

mylist = ['100.122.133.111','101.122.133.111']
print(mylist)
number = int(input("Enter the number to display:"))
print("You chose ", mylist[number])
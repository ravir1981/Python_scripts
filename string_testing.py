"""
string = '''Have a good Day'''
print(type(string))

### both will yield same result
print(string[-1])
print(string[14])
print("Print the last word: ", string[12:])

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


mylist = ['100.122.133.111','101.122.133.111']
print(mylist)
number = int(input("Enter the number to display:"))
print("You chose ", mylist[number])


kg = float(input("Enter the number to convert:"))
lbs = kg * 2.2
print("LBS: ", lbs)


# List Comprehension

filenames = ["1.Raw Data.txt", "2.Human organs.txt", "3.The world.txt"]

filenames = [filename.replace('.','-', 1) for filename in filenames]
print(filenames)

old = [1,2,3]
new = [i + 10 for i in old]
print("New value : ", new)

# capitalize fn and ln
names = ["john smith", "ray ludi", "eva kuki"]
names = [name.title() for name in names]
print(names)

# find the total character of each string
usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(user) for user in usernames]
print(usernames)

# print the entry in float
user_entries = ['10', '19.1', '20']
user_entries = [float(entry) for entry in user_entries]
print(user_entries)

# Find the sum of numbers
user_entries = ['10', '19.1', '20']
#print(sum(map(float, user_entries)))

user_entries = sum([float(number) for number in user_entries])
print("User Entry : ", user_entries)



def func(a):
    if a < 2:
        return a
    print(a + func(a - 1))
    return a + func(a - 1)


print(func(4))
"""

print(36 << 3)

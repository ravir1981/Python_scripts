file = open('Files/members.txt', 'r')
contents = file.readlines()
file.close()
print(contents)

prompt = input("Enter the str:")
contents.append("\n")
contents.append(prompt)
file = open('Files/members.txt', 'w')
file.writelines(contents)
file.close()

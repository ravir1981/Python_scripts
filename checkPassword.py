password = input("Enter the password:")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

flag = False

for char in password:
    if char.isdigit():
        flag = True

result["digit"] = flag

upperC = False
for upp in password:
    if upp.isupper():
        upperC = True

result["upper"] = upperC
# Another way instead of using Dictionary
# result = []
# #result.append(upperC)

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password.", result.values())

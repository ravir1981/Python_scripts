user_ip = "Enter a value:"

var = "True"
todos = []

# while var:
#     todo = input(user_ip)
#     #newValue = todo.capitalize()
#     newValue = todo.title()
#     print(newValue)
#     todos.append(newValue)
#     print(todos)
#     #var = False

password = input("Enter Password:")

while password != "pass123":
    password = input("Enter the password again:")

print("Correct Password is ", password)
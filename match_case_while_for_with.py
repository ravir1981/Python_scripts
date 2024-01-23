from pathlib import Path

todos = []

while True:
    user_action = input("Enter the value Add or Edit or Drop or Show/Display or Exit:")
    user_action.lower()
    user_action = user_action.strip()
    my_file = Path('/Users/ravindranradhakrishnan/Documents/Python/Udemy/pythonProject/todo.txt')

    match user_action:
        case 'add':
            todo = input("Enter the value:") + "\n"

            if my_file.is_file():
                with open(my_file, 'r') as file:
                    todos = file.readlines()

                todos.append(todo)

                with open(my_file, 'w') as file:
                    file.writelines(todos)
            else:
                todos.append(todo)
                with open(my_file, 'w') as file: # This is called context-manager
                    file.writelines(todos)

        case 'show' | 'display':

            with open(my_file, 'r') as file:
                todos = file.readlines()

            """
            # list comprehensions
            new_todos = [item.strip('\n') for item in todos]


            # different approach
            new_todos = []
            for item in todos:
                new_item = item.strip("\n")
                new_todos.append(new_item)
            """

            for index, item in enumerate(todos):
                item = item.strip('\n') # stripping
                item.title()
                print(f"{index + 1}-{item}")
        case 'edit':
            with open(my_file, 'r') as file:
                todos = file.readlines()

            number = input("Enter the number to get the value from list:")
            number = int(number) - 1

            print("Value which is getting modified is : ", todos[number])
            new_val = input("Enter the new value:")
            todos[number] = new_val + "\n"

            with open(my_file, 'w') as file:
                file.writelines(todos)

        case 'drop':
            with open(my_file, 'r') as file:
                todos = file.readlines()

            number = int(input("Enter the number to drop the value from list:"))
            number -= 1
            print("Item to be dropped is : ", todos[number].strip('\n'))
            todos.pop(number)

            with open(my_file, 'w') as file:
                file.writelines(todos)
        case 'exit' | 'e':
            break
        case _:
            print("Unexpected command, Enter the correct type.")

print("Program Complete")

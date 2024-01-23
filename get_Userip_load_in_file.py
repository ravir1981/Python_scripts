from pathlib import Path

todos = []


def get_input():
    with open(my_file, 'r') as file:
        todos = file.readlines()
    return todos


while True:
    user_action = input("Enter the value Add or Edit or Drop or Show/Display or Exit:")
    user_action.lower()
    user_action = user_action.strip()
    my_file = Path('/Users/ravindranradhakrishnan/Documents/Python/Udemy/pythonProject/todo.txt')

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        print("Todo is :", todo)

        if my_file.is_file():
            todos = get_input()

            todos.append(todo)
            print(todos)

            with open(my_file, 'w') as file:
                file.writelines(todos)
        else:
            todos.append(todo)
            with open(my_file, 'w') as file:  # This is called context-manager
                file.writelines(todos)
    elif user_action.startswith("show"):
        todos = get_input()

        """
        # list comprehensions
        new_todos = [item.strip('\n') for item in todos]
        """

        for index, item in enumerate(todos):
            item = item.strip('\n')  # stripping
            item.title()
            print(f"{index + 1}-{item}")
    elif user_action.startswith("edit"):
        try:
            todos = get_input()

            number = int(user_action[5:])
            number = int(number) - 1

            print("Value which is getting modified is : ", todos[number])
            new_val = input("Enter the new value:")
            todos[number] = new_val + "\n"

            with open(my_file, 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Wrong input. Enter the correct input.")
            continue
        except IndexError:
            print(f"Total items in the file is {len(todos)}. Enter the correct index.")
            continue
    elif user_action.startswith("drop"):
        try:
            todos = get_input()

            number = int(user_action[5:])
            number -= 1
            print("Item to be dropped is : ", todos[number].strip('\n'))
            todos.pop(number)

            with open(my_file, 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("The provided index is not available in existing List.")
            print(f"Total items in the file is {len(todos)}")
            continue
    elif 'exit' in user_action or 'e' in user_action:
        break
    else:
        print("Wrong Input Actions. Enter the correct input option again\n")

print("User is", user_action)
print("Program Complete")

from pathlib import Path
from Modules import user_inputs

#from user_inputs import get_input, write_todos

# print(help(write_todos)) # Use of doc-strings
todos = []

while True:
    user_action = input("Enter the value Add or Edit or Drop or Show/Display or Exit:")
    user_action.lower()
    user_action = user_action.strip()
    my_file = Path('/Users/ravindranradhakrishnan/Documents/Python/Udemy/pythonProject/todo.txt')

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        print("Todo is :", todo)

        if my_file.is_file():
            todos = user_inputs.get_input(my_file)

            todos.append(todo)
            print(todos)

            user_inputs.write_todos(todos, my_file)
        else:
            todos.append(todo)
            user_inputs.write_todos(todos)
    elif user_action.startswith("show"):
        todos = user_inputs.get_input(my_file)

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
            todos = user_inputs.get_input(my_file)

            number = int(user_action[5:])
            number = int(number) - 1

            print("Value which is getting modified is : ", todos[number])
            new_val = input("Enter the new value:")
            todos[number] = new_val + "\n"

            user_inputs.write_todos(todos, my_file)
        except ValueError:
            print("Wrong input. Enter the correct input.")
            continue
        except IndexError:
            print(f"Total items in the file is {len(todos)}. Enter the correct index.")
            continue
    elif user_action.startswith("drop"):
        try:
            todos = user_inputs.get_input(my_file)

            number = int(user_action[5:])
            number -= 1
            print("Item to be dropped is : ", todos[number].strip('\n'))
            todos.pop(number)

            user_inputs.write_todos(todos, my_file)
        except IndexError:
            print("The provided index is not available in existing List.")
            print(f"Total items in the file is {len(todos)}")
            continue
    elif 'exit' in user_action or 'e' in user_action:
        break
    else:
        print("Wrong Input Actions. Enter the correct input option again\n")

print("User action is", user_action)
print("Program Complete")

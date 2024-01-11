todos = []

while True:
    user_action = input("Enter the value Add or Edit or Drop or Show/Display or Exit:")
    user_action.lower()
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter the value:")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                item.title()
                print(f"{index + 1}-{item}")
        case 'edit':
            number = input("Enter the number to get the value from list:")
            number = int(number) - 1
            new_val = input("Enter the new value:")
            todos[number] = new_val
        case 'drop':
            number = int(input("Enter the number to drop the value from list:"))
            todos.pop(number - 1)
        case 'exit' | 'e':
            break
        case _:
            print("Unexpected command, Enter the correct type.")

print("Program Complete")

from Modules import user_inputs
import PySimpleGUI
from pathlib import Path
import time

PySimpleGUI.theme('DarkPurple4')
clock = PySimpleGUI.Text('', key='clock')
label = PySimpleGUI.Text("Type in a to-do:")
input_box = PySimpleGUI.InputText(tooltip="Enter todo items!", key="todo")
add_button = PySimpleGUI.Button("Add")
my_file = Path('/Users/ravindranradhakrishnan/Documents/Python/Udemy/pythonProject/todo.txt')

list_box = PySimpleGUI.Listbox(values=user_inputs.get_input(my_file),
                               key='todos',
                               enable_events=True, size=(45, 10))
edit_button = PySimpleGUI.Button("Edit")
drop_button = PySimpleGUI.Button("Drop")
exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window('My TODO App',
                            [[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, drop_button],
                             [exit_button]],
                            font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%m/%d/%Y-%H:%M:%S"))
    print(1, event)
    print(2, values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = user_inputs.get_input(my_file)
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            window['todos'].update(values=todos)
            user_inputs.write_todos(todos, my_file)
        case "Edit":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo']

                todos = user_inputs.get_input(my_file)
                index = todos.index(todo_edit)
                todos[index] = new_todo
                user_inputs.write_todos(todos, my_file)
                window['todos'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please select an item first!", font=('Helvetica', 20))
        case "Drop":
            try:
                todo_drop = values['todos'][0]
                todos = user_inputs.get_input(my_file)
                todos.remove(todo_drop)
                user_inputs.write_todos(todos, my_file)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                PySimpleGUI.popup("Please select an item first to drop!!!", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()

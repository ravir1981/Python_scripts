from Modules import user_inputs
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do:")
input_box = PySimpleGUI.InputText(tooltip="Enter todo items!")
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window('My TODO App', [[label],[input_box,add_button]])
window.read()
window.close()
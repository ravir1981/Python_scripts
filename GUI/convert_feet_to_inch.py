import PySimpleGUI
from Modules.converter import convert_meter

feet_label = PySimpleGUI.Text("Enter Feet:")
input_feet = PySimpleGUI.InputText(tooltip="Enter the Integer", key="feet")
inch_label = PySimpleGUI.Text("Enter Inch:")
input_inch = PySimpleGUI.InputText(tooltip="Enter the Integer", key="inch")

convert_button = PySimpleGUI.Button("Convert")
output_label = PySimpleGUI.Text(key='output',text_color="red")

window = PySimpleGUI.Window("My feet to inch Converter", layout=[[feet_label, input_feet],
                                                                 [inch_label, input_inch],
                                                                 [convert_button, output_label]],
                            font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            feet = float(values['feet'])
            inch = float(values['inch'])
            print(feet,inch)
            meter = convert_meter(feet,inch)
            window['output'].update(value=meter)
            # window["output"].update(value=f"{meter} m", text_color="red")
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
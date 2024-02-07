import PySimpleGUI
import Modules.compressor

label1 = PySimpleGUI.Text("Select the file to compress:", key="files")
input1 = PySimpleGUI.Input()
button1 = PySimpleGUI.FilesBrowse("Chose")

label2 = PySimpleGUI.Text("Select the destination folder:", key="folder")
input2 = PySimpleGUI.Input()
button2 = PySimpleGUI.FolderBrowse("Chose")

compress_button = PySimpleGUI.Button("Compress")

window = PySimpleGUI.Window("File Compressor",
                            layout=[[label1, input1, button1],
                                    [label2, input2, button2],
                                    [compress_button]])

while True:
    event, values = window.read()
    print(event,values)
    filePath = values['files'].split(";")
    folderPath = values['folder']

window.close()
import PySimpleGUI as pg

label1 = pg.Text("Select the file to compress:")
input1 = pg.Input()
button1 = pg.FilesBrowse("Chose")

label2 = pg.Text("Select the destination folder:")
input2 = pg.Input()
button2 = pg.FolderBrowse("Chose")

compress_button = pg.Button("Compress")

window = pg.Window("File Compressor", layout=[[label1,input1,button1],
                                                   [label2,input2,button2],
                                                   [compress_button]])
window.read()
window.close()
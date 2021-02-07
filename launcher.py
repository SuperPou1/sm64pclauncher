import PySimpleGUI as sg
import os
options=[
    [sg.Button('Play', size=(15, 3), button_color=("white", "green"))],
    [sg.Button('Build', size=(15, 1))]
]
buildselect=[[
    sg.Text('Select your sm64pc build:'),
],
[
    sg.Listbox(
        values=[], enable_events=True, size=(40, 20), key="Build list"
    )
]
]
layout = [
    [
        sg.Column(buildselect, size=(300, 300)),
        sg.VSeperator(),
        sg.Column(options,size=(140, 300)),
    ]
]
window = sg.Window('SM64pc launcher', layout)
while True:
    event, values = window.read()
    if event == "Play" or event == sg.WIN_CLOSED:
        break
    if event == 'Build':
        import builder
        exit()

import PySimpleGUI as sg
import os
options=[
    [sg.Button('Play')]
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
        sg.Column(buildselect),
        sg.VSeperator(),
        sg.Column(options),
    ]
]
window = sg.Window('SM64pc launcher', layout)
while True:
    event, values = window.read()
    if event == "Play" or event == sg.WIN_CLOSED:
        break

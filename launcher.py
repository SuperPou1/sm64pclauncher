import PySimpleGUI as sg
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

with open('builds.txt', 'r') as blist:
    builds = blist.readlines()

url = "https://raw.githubusercontent.com/SuperPou1/sm64pclauncher/main/news.txt"
html = urlopen(url).read()
newstext = BeautifulSoup(html, features="html.parser")
newstext = newstext.get_text()

news=[
    [sg.Text('News', font=(1))],
    [sg.Text(newstext, border_width=250)]
    ]
options=[
    [sg.Button('Play', size=(10, 2), button_color=("white", "green"),font=(1),disabled=True)],
    [sg.Button('Build', size=(14, 1))]
]
buildselect=[[
    sg.Text('Select your sm64pc build:'),
],
[
    sg.Listbox(
        values=builds, enable_events=True,select_mode='single', size=(40, 20), key="buildlist", bind_return_key = True
    )
]
]
layout = [
    [
        sg.theme_background_color(),
        sg.Column(buildselect, size=(300, 300)),
        sg.VSeperator(),
        sg.Column(options,size=(140, 300)),
        sg.VSeparator(),
        sg.Column(news, size=(300, 300)),
    ]
]
window = sg.Window('SM64pc launcher', layout)
while True:
    event, values = window.read()
    if event == 'buildlist':
        buildselected = os.path.join(
            values['buildlist'][0]
        )

        buildselected = buildselected.rstrip("\n")
        if buildselected == "":
            window['Play'].update(disabled=True)
        if not buildselected == "":
            window["Play"].update(disabled=False)
    if event == "Play":
        os.system('cd "'+buildselected+'/build/us_pc/" && ./sm64.us.f3dex2e')
        break
        
    if event == 'Build':
        import builder
        exit() 
    if event == sg.WIN_CLOSED:
        exit()

        

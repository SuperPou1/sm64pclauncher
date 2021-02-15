# hello_psg.py

import PySimpleGUI as sg
import os
import subprocess
import shlex

buildfailed = [[sg.Text('Build failed, try to build again'), sg.Button('Ok')]]
branchselect = [[sg.Text("Paste github link to sm64pc repo and branch")],[sg.In(),sg.In(size=(7, 1))],[sg.Text("And type the name of repo folder")],[sg.In()],[sg.Text('modelpack folder (optional)')],[sg.In(),sg.FolderBrowse()],[sg.Text('Texture pack folder (optional)')],[sg.In(),sg.FolderBrowse()],[sg.Button("Ok")]]
buildoptions = [[sg.Text('specify build flags and jobs, you can see possible flags on your repo\'s wiki, if you use modelpack, use MODELPACK=1, if you use texturepack, use EXTERNAL_DATA=1')],[sg.InputText(),sg.Button('Build')]]
baseromselect = [[sg.Text("Select baserom of sm64 with extension .z64")],[
        sg.Text("baserom:"),
        sg.In(),
        sg.FileBrowse(),

    ],[sg.Button("Ok")]]

msys2folderselect=[
    [sg.Text('Select your msys2 folder')],
    [
        sg.In(),
        sg.FolderBrowse()
    ],[sg.Checkbox(text='install msys2 dependencies (check if you are building for the first time)', key='msys2depends')],
    [sg.Button('Ok')]
]
if os.name == "nt":
    window = sg.Window('Windows detected', msys2folderselect)
    while True:
        event,  values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == "Ok":
            msys2folder = values[0].replace('/', '\\')
            window.close()
            msys2depends = values['msys2depends']
            break
            





def run(command):
    if os.name == "nt":
        return subprocess.run(
            [
                msys2folder+"/usr/bin/bash.exe",
                "--login",
                "-c",
                command,
            ],
            encoding="utf-8",
            env={**os.environ, "MSYSTEM": "MINGW64", "CHERE_INVOKING": "yes"},
        ).returncode
    else:
        return subprocess.run(
            command,
            shell=True,
        ).returncode
if os.name == 'nt' and msys2depends == True:
    run('pacman -S mingw-w64-x86_64-SDL2')

# Create the window
window = sg.Window("SM64 pc builder", branchselect)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Ok" or event == sg.WIN_CLOSED:
        branchname=values[1]
        if os.name == 'posix':
            os.system('git clone "'+values[0]+'" "'+values[2]+'" --branch='+values[1])
            os.system('cp -r "'+values[3]+'/actors" "'+values[2]+'" && cp -r "'+values[3]+'/src" "'+values[2]+'"')
        if os.name == 'nt':
            run('git clone "'+values[0]+'" "'+values[2]+'" --branch='+values[1])
            run('cp -r "'+values[3]+'/actors" "'+values[2]+'" && cp -r "'+values[3]+'/src" "'+values[2]+'"')
            run('dir')
        repofolder=values[2]
        texturepack=values[4]
        window.close()
        window = sg.Window("baserom", baseromselect)
        
        while True:
            event, values = window.read()
            if event == 'Ok' or event == sg.WIN_CLOSED: 
                baseromfolder=values[0]
                window.close()
                window = sg.Window('build options', buildoptions)
                event, values = window.read()
                if event == 'Build' or event == sg.WIN_CLOSED:
                    buildflags = values[0]
                    print(buildflags)
                    window.close
                    break



    window.close()

    if os.name == 'posix':
        os.system('cp "'+baseromfolder+'" "'+repofolder+'/baserom.us.z64"')
        os.system('cd "'+repofolder+'" && make '+buildflags)
        os.system('cp -r "'+texturepack+'/gfx" "'+repofolder+'/build/us_pc/res"')
    
    if os.name == 'nt':
        run('dir')
        run('cp "'+baseromfolder+'" "'+repofolder+'/baserom.us.z64"')
        run('cd "'+repofolder+'" && make '+buildflags)
        run('cp -r "'+texturepack+'/gfx" "'+repofolder+'/build/us_pc/res"')
    with open('builds.txt', 'r') as blist:
        builds = blist.read()
    with open ('builds.txt', 'w') as bwrite:
        bwrite.write(repofolder+'\n'+builds)
    if os.path.exists(repofolder+'/build/us_pc/sm64.us.f3dex2e.exe') == False:
        window = sg.Window('Build failed! :(', buildfailed)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok':
                exit()
    if os.name == 'posix':
        os.system('."/'+repofolder+'/build/us_pc/sm64.us.f3dex2e"')
    if os.name == 'nt':
        os.system('"'+repofolder+'\\build\\us_pc\\sm64.us.f3dex2e.exe"')
    exit()



        

        




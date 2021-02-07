# sm64pclauncher
A launcher for super mario 64 pc port. only works on linux (at the moment, later it will work on windows too)
## installation
First, you will need python 3 and python pip. when you have python 3 and pip installed, install the rest of dependencies using installdepends.sh.
to install sm64pc launcher (in terminal):
install python 3, diffierent command on diffierent distros
`python3 get-pip.py`
`git clone https://github.com/SuperPou1/sm64pclauncher`
`cd sm64pclauncher`
`chmod +x installdepends.sh`
`./installdepends.sh`
`python3 launcher.py`
## Usage
To run the launcher, type in terminal `python3 launcher.py`  
To build sm64, press "Build"  
To play, select existing build and click "Play"  
## How to build
In the first input box, paste github repository of any sm64pc, and in the box next to the first one type the branch.  
In the second box, type any name you want for your repo folder. it will display like that in the launcher build selection.  
In the other two boxes you can specify modelpack and texture pack folder. Note: when you browse for the folder, you have to be in this folder to select it.  
Click "Ok". it will freeze for a while this is because it is downloading the repo.  
Click "Browse" and find your Super Mario 64 USA rom. Click "Ok"  
Specify the build flags, you can find which build flags are avaible for your repo by cheking the makefile or checking your repo's wiki if it exists. Remember to add "-j4" for faster building speed.  
Click "Build". Now wait patiently for the build to finish. When it finishes, game should lauch shortly after. If you see a text box and the game does not launch for like 2 minutes, it means that your build failed. delete the repo folder and try to build again. If the game launches, it is ok. When you restart the launcher, it should show the new build on the list.
### Tip
if you want a shortcut to the laucher, on ubuntu, you can do this by making a file called `sm64launcher.desktop` in `/home/username/.local/share/applications/` containing the following:  
`[Desktop Entry]`  
`Name=SM64 launcher`  
`Type=Application`  
`Exec=bash -c "cd /home/superpou1/mariolauncher/ && python3 /home/superpou1/mariolauncher/launcher.py"`  
`Icon=/whatever/icon/you/like`  
`Categories=Game;`  

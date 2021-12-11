# sm64pclauncher
A launcher for super mario 64 pc port. works on linux apt/pacman based distros and Windows.
## Linux installation
1.download latest release and unpack it  
2.run these commands in terminal:  
`cd /directory/to/your/downloaded/launcher` (replace "/directory/to/your/downloaded/launcher" with your directory to the launcher)  
`chmod +x installdepends.sh`  
`chmod +x launcher.py`    
`chmod +x builder.py`    
`./installdepends.sh`  
## Windows installation
install [python 3](https://www.python.org/downloads/) and [msys2](https://www.msys2.org/), then download the latest release and unpack it, then doubleclick on `installdepends.bat`.
## Usage
### Running on Windows
doubleclick  on `launcher.py`
### Running on Linux
type in terminal `python3 launcher.py` (you must be in launcher directory)  
or  
doubleclick  on `launcher.py` (this way may not work)
### Using it
To build sm64, press "Build"  
To play, select existing build and click "Play"  
## How to build
If you are on windows, you should see a window prompting to select the msys2 folder. Basicallly you need to select the folder where you installed msys2. If you are building for the first time or reinstalled msys2, check install msys2 dependencies.  
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
`Exec=bash -c "cd path/into/sm64pclauncher ; ./launcher.py"`  
`Icon=/whatever/icon/you/like`  
`Categories=Game;`  
(it may not work on other distros, but it is worth trying!)  
on windows right click the file launcher.py and select create shortcut and move it to desktop, and change the icon it you want

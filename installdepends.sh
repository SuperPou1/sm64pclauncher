#!/bin/bash

until [[ ${ANSWER,,} == "pacman" ]] || [[ ${ANSWER,,} == "apt" ]]; do
	read -p "Use pacman or apt? " ANSWER
done

if [[ ${ANSWER,,} == "pacman" ]]; then
	sudo pacman -S python3 python-pip tk sdl2_gfx sdl2_image sdl2_mixer sdl2_net git
else
	sudo apt-get install -y python3 python3-pip python3-tk libsdl2-dev git
fi

pip3 install pysimplegui

#!/bin/bash

word=$(rofi -dmenu -p "Enter a word")

if [[ -z "$word" ]]; then
    exit 1
fi

output=$(python3 /home/ucenik/Workplace/cevirmen/cevirmen.py "$word")

zenity --info --text="$output" --title="Output"

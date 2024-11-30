#!/bin/bash

# Prompt the user for input using zenity
word=$(zenity --entry --title="Input Required" --text="Enter a word:")

# Exit if no word is entered (e.g., user cancels)
if [[ -z "$word" ]]; then
    exit 1
fi

# Run your application and capture the output
output=$(python3 ./cevirmen.py "$word")

# Display the output using zenity
zenity --info --title="Output" --text="$output"

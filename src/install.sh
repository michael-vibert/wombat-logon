#!/bin/bash
pip install -r requirements.txt
# from https://edstem.org/au/courses/10081/lessons/27592/slides/194999 check python installed and gracefully exit if not!
if ! [[ -x "$(command -v python)" ]]
then
    echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
    exit 1
else
    echo 'You have the correct Python program to run this program - Lets Go!'
fi
python3 main.py
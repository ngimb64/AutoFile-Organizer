# AutoFile-Organizer
![alt text](https://github.com/ngimb64/AutoFile-Organizer/blob/main/AutoFileOrganizer.gif?raw=true)
![alt text](https://github.com/ngimb64/AutoFile-Organizer/blob/main/AutoFileOrganizer.png?raw=true)

## Prereqs
> This program runs on Windows and Linux, written in Python 3.9

## Purpose
> Monitors source folder and automatically backs up data put in source folder to destination folder by file extension type.

## Installation
- Run the setup.py script to build a virtual environment and install all external packages in the created venv.

> Example:<br>
> python3 setup.py "venv name"

- Once virtual env is built traverse to the (Scripts-Windows or bin-Linux) directory in the environment folder just created.
- For Windows in the Scripts directory, for execute the "activate" script to activate the virtual environment.
- For Linux in the bin directory, run the command `source activate` to activate the virtual environment.

## How to use
- Open up Command Prompt (CMD) or terminal
- Enter the directory containing the program and execute in shell
- To organize files, move files to the directory defined by the SRC\_DIR macro.

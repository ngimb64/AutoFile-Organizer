<div align="center" style="font-family: monospace">
<h1>AutoFile-Organizer</h1>
&#9745;&#65039; Bandit verified &nbsp;|&nbsp; &#9745;&#65039; Synk verified &nbsp;|&nbsp; &#9745;&#65039; Pylint verified 10/10
</div><br>

![alt text](https://github.com/ngimb64/AutoFile-Organizer/blob/main/AutoFileOrganizer.gif?raw=true)
![alt text](https://github.com/ngimb64/AutoFile-Organizer/blob/main/AutoFileOrganizer.png?raw=true)

## Purpose
Monitors source folder and automatically organizes any introduced files by moving them to they're designated destination folder based on file extension.

### License
The program is licensed under [GNU Public License v3.0](LICENSE.md)

### Contributions or Issues
[CONTRIBUTING](CONTRIBUTING.md)

## Prereqs
This program runs on Windows 10 and Debian-based Linux, written in Python 3.9 and updated to version 3.10.6

## Installation
- Run the setup.py script to build a virtual environment and install all external packages in the created venv.

> Examples:<br> 
>       &emsp;&emsp;- Windows:  `python setup.py venv`<br>
>       &emsp;&emsp;- Linux:  `python3 setup.py venv`

- Once virtual env is built traverse to the (Scripts-Windows or bin-Linux) directory in the environment folder just created.
- For Windows, in the venv\Scripts directory, execute `activate` or `activate.bat` script to activate the virtual environment.
- For Linux, in the venv/bin directory, execute `source activate` to activate the virtual environment.
- If for some reason issues are experienced with the setup script, the alternative is to manually create an environment, activate it, then run pip install -r packages.txt in project root.
- To exit from the virtual environment when finished, execute `deactivate`.

## How to use
- Once in the activated virtual environment, enter the directory containing the program and execute in shell.
- To organize files, move files to the directory defined by the SRC_DIR and they will be automatically organized based on file extension.

## Function Layout
-- autofile_organizer.py --
> BackupHandler &nbsp;-&nbsp; Class is trigger when the monitored SRC_DIR detects modification.<br>
> on_modified &nbsp;-&nbsp; Copies contents of source dir to dest dir on event detection per 
> modification.

> main &nbsp;-&nbsp; Facilitates file system handler, copies data to desired folders based on file 
> extension. 
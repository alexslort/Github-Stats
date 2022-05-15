# Github-Stats
This program creates an API endpoint that displays aggregated statistics accross all of a specified users repositories

USE A VIRTUAL ENVIRONMENT

In the project folder, set up a virtual environment using commands below in the terminal
- Linux
  > sudo apt-get install python3-venv    # If needed
  > 
  > python3 -m venv .venv
  > 
  > source .venv/bin/activate

- macOS
  > python3 -m venv .venv
  > 
  > source .venv/bin/activate

- Windows
  > py -3 -m venv .venv
  > 
  > .venv\scripts\activate
  > 
use interpreter that contains ('.venv': venv) -VScode

INSTALL INSTRUCTIONS 

 while (.venv) is active, in the project folder, open terminal and install:
 > pip install flask
 > 
 > pip install PyGithub

HOW TO RUN ENDPOINT

 In terminal window, set FLASK_APP equal to application file
  - Mac, Linux:
    > export FLASK_APP=gitAPI.py
    > 
    > flask run
  - Windows CMD:
    > set FLASK_APP=gitAPI.py
    > 
    > flask run
  - powershell:
    > $env:FLASK_APP = "gitAPI.py"
    > 
    > flask run
 Do this each time you open a new terminal

 paste http link into browser and include "/usernamehere" after address ex. http://123.0.0.1:5000/alexslort

 For statistics of repositories that have no forks, do "/usernamehere/forked"

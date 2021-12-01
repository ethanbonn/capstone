# setup

Prereqs:
- Install freecad https://www.freecadweb.org/
- Make sure you have python 3.8 installed https://www.python.org/downloads/

1. create a directory on your computer called 'capstone'
2. run "pip install virtualenv"
3. Add virtualenv to path
4. run "virtualenv venv -p python38"
5. # For Unix/Linux based, type:
source venv/bin/activate
5. # For Windows, type:
   run "cd venv/Scripts/"
   then run "activate"
   then "cd../../"
6. run "git clone https://github.com/ethanbonn/capstone.git" (Make sure you are in the capstone root directory")
7. run "pip install -r requirements.txt"
8. Create a ".env" file 
9. Find where the freecad downloaded it's "FreeCad 0.19/bin" file (mine was "C:/Program Files/FreeCAD 0.19/bin/")
10. (In the .env file) Add the above file path to the variable "FREE CAD = "


The test to see if everything works is:
11. run "python capstone.py" and get no errors

you should be good to go, lmk if you run into any problems

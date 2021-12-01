from dotenv import load_dotenv
load_dotenv(".env")
import os
import sys
FREECADPATH = os.environ.get("FREECAD")
sys.path.append(FREECADPATH) 
import FreeCAD
import otsun


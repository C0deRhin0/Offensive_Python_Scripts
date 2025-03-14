import PyInstaller.__main__
import shutil
import os

filename= "malicious.py" 
exename = "rhino.exe" 
icon = "chrome.ico"
pwd = os.getcwd()

if os.path.isfile(exename):
  os.remove(exename)

if os.path.exists("__pycache__"):
    shutil.rmtree("__pycache__")

PyInstaller.__main__.run([
  "malicious.py", 
  "--onefile", 
  "--clean",
  "--log-level=ERROR", 
  "--name="+exename, 
  "--icon="+icon
])

shutil.move(os.path.join(pwd, "dist", exename), pwd) 
shutil.rmtree("dist")
shutil.rmtree("build")
os.remove(exename+".spec")

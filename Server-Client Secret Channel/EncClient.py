import socket, os
from Crypto.Cipher import AES

HOST = "127.0.0.1"
PORT = 8334
KEY = b"RhinoiIiRhinoiIi"

def encrypt_message(message, key, iv):
    message += " " * (16 - len(message) % 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(bytes(message, "utf-8"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    while True:
        message = input("Enter message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        
        iv = os.urandom(16)
        client_socket.send(iv)
        client_socket.send(bytes([len(message)]))
        encrypted_message = encrypt_message(message, KEY, iv)
        print(f"Sending encrypted: {encrypted_message.hex()}")
        client_socket.sendall(encrypted_message)

    print("Closing connection...")

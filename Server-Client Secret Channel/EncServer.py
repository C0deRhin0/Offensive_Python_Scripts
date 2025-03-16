import socket
from Crypto.Cipher import AES

HOST = "127.0.0.1"
PORT = 8334
KEY = b"RhinoiIiRhinoiIi"

def decrypt_message(encrypted_data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(encrypted_data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    with conn:
        while True:
            iv = conn.recv(16)
            if not iv:
                break

            length = conn.recv(1)
            if not length:
                break
            
            length = ord(length)
            encrypted_data = conn.recv(1024)
            if not encrypted_data:
                break

            decrypted_message = decrypt_message(encrypted_data, KEY, iv).decode("utf-8")[:length]
            print(f"Received: {decrypted_message}")

        print("Connection closed.")

import socket
import datetime

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 2222       # Choose a port to mimic (like SSH)

def log_attempt(addr, data):
    with open('honeypot.log', 'a') as f:
        f.write(f"{datetime.datetime.now()} - Connection from {addr} - Data: {data}\n")

def start_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Honeypot listening on port {PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {addr}")
                data = conn.recv(1024)
                log_attempt(addr[0], data.decode(errors='ignore'))
                conn.sendall(b"Welcome to this totally legit server!\n")

if __name__ == "__main__":
    start_honeypot()

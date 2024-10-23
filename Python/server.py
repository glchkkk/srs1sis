import socket
from _thread import *

clients = []

def clientthread(conn, addr):
        message = conn.recv(1024).decode()
        if message:
                print(f"[{addr}] {message}")
                cast(message, conn)
    
def cast(message, connection):
    for client in clients:
        if client != connection:
            client.send(message.encode())

server = socket.socket()
hostname = socket.gethostname()
port = 12345
server.bind((hostname, port))
server.listen(5)

print("server running...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print(f"new connection: {addr}")
    start_new_thread(clientthread, (conn, addr,))
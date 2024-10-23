import socket
import threading

def messages(client):
    message = client.recv(1024).decode()
    if message:
       print(message)

client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

while True:
    message = input()
    client.send(message.encode())

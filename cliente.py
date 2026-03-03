import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            msg = client.recv(1024)
            print(msg.decode())
        except:
            break

threading.Thread(target=receive_messages).start()

while True:
    message = input()
    client.sendall(message.encode())
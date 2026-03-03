import socket

HOST = '127.0.0.1'  # IP do servidor (localhost)
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b"Ola servidor!")
data = client.recv(1024)

print("Resposta do servidor:", data.decode())

client.close()

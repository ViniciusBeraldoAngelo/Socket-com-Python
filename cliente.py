import socket

<<<<<<< HEAD
HOST = '127.0.0.1'  # IP do servidor (localhost)
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b"Ola servidor!")
data = client.recv(1024)

print("Resposta do servidor:", data.decode())

client.close()
=======
HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

mensagem = input("Digite uma mensagem para o servidor: ")

cliente.sendall(mensagem.encode())

resposta = cliente.recv(1024)

print("Servidor respondeu:", resposta.decode())

cliente.close()
>>>>>>> 5dca386bc797ea0abd2a1a7d89405177a5154711

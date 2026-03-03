import socket

HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

mensagem = input("Digite uma mensagem para o servidor: ")

cliente.sendall(mensagem.encode())

resposta = cliente.recv(1024)

print("Servidor respondeu:", resposta.decode())

cliente.close()
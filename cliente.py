import socket

HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

while True:
    mensagem = input("Você: ")
    
    if mensagem.lower() == "sair":
        break

    cliente.sendall(mensagem.encode())

    resposta = cliente.recv(1024)

    print("Servidor:", resposta.decode())

cliente.close()
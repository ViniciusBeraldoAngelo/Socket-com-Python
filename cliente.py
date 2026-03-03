import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            print(mensagem)
        except:
            print("Conexão encerrada.")
            cliente.close()
            break

def enviar_mensagens(cliente):
    while True:
        mensagem = input()
        cliente.send(mensagem.encode())

        if mensagem.lower() == "sair":
            cliente.close()
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    nome = input("Digite seu nome: ")
    cliente.send(nome.encode())

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread_receber.start()

    enviar_mensagens(cliente)

iniciar_cliente()
import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

clientes = []
nomes = {}

def broadcast(mensagem):
    for cliente in clientes:
        try:
            cliente.send(mensagem.encode())
        except:
            remover_cliente(cliente)

def remover_cliente(cliente):
    if cliente in clientes:
        nome = nomes.get(cliente, "Desconhecido")
        clientes.remove(cliente)
        cliente.close()
        print(f"{nome} saiu do chat.")
        broadcast(f"{nome} saiu do chat.")
        nomes.pop(cliente, None)

def lidar_cliente(cliente):
    try:
        nome = cliente.recv(1024).decode()
        nomes[cliente] = nome
        clientes.append(cliente)

        print(f"{nome} entrou no chat.")
        broadcast(f"{nome} entrou no chat.")

        while True:
            mensagem = cliente.recv(1024).decode()

            if mensagem.lower() == "sair":
                remover_cliente(cliente)
                break

            mensagem_formatada = f"{nome}: {mensagem}"
            print(mensagem_formatada)
            broadcast(mensagem_formatada)

    except:
        remover_cliente(cliente)

def enviar_mensagem_servidor():
    while True:
        mensagem = input()
        mensagem_formatada = f"[SERVIDOR]: {mensagem}"
        print(mensagem_formatada)
        broadcast(mensagem_formatada)

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print("Servidor iniciado...")

    # Thread para o servidor poder falar
    thread_input = threading.Thread(target=enviar_mensagem_servidor)
    thread_input.daemon = True
    thread_input.start()

    while True:
        cliente, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_cliente, args=(cliente,))
        thread.start()

iniciar_servidor()
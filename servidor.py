import socket
<<<<<<< HEAD
import threading

HOST = '0.0.0.0'
PORT = 5000

clients = []

def handle_client(conn, addr):
    print(f"Novo cliente conectado: {addr}")
    clients.append(conn)

    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break

            print(f"{addr}: {msg.decode()}")

            # envia mensagem para todos os outros clientes
            for client in clients:
                if client != conn:
                    client.sendall(msg)

        except:
            break

    print(f"Cliente desconectado: {addr}")
    clients.remove(conn)
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Servidor rodando...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
=======

HOST = '127.0.0.1'  # endereço local
PORT = 5000         # porta de comunicação

# cria o socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa o socket ao endereço e porta
servidor.bind((HOST, PORT))

# coloca o servidor para ouvir conexões
servidor.listen()

print("Servidor aguardando conexão...")

# aceita conexão do cliente
conn, addr = servidor.accept()

print(f"Conectado por {addr}")

while True:
    dados = conn.recv(1024)
    if not dados:
        break
    
    mensagem = dados.decode()
    print("Cliente:", mensagem)
    
    resposta = "Mensagem recebida com sucesso!"
    conn.sendall(resposta.encode())

conn.close()

>>>>>>> 5dca386bc797ea0abd2a1a7d89405177a5154711

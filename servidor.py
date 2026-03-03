import socket
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
import socket

HOST = '127.0.0.1'
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORT))

servidor.listen()

print("Servidor aguardando conexão...")

conn, addr = servidor.accept()

print(f"Conectado por {addr}")

while True:
    dados = conn.recv(1024)

    if not dados:
        break

    mensagem = dados.decode()
    print("Cliente:", mensagem)

    if mensagem.lower() == "sair":
        print("Encerrando conexão...")
        break

    resposta = input("Você: ")
    conn.sendall(resposta.encode())

conn.close()
servidor.close()
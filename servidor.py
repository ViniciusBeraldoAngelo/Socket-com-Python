import socket

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


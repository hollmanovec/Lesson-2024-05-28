import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))
server_socket.listen()


print("Server čaká na pripojenia...")
client_socket, client_address = server_socket.accept()
print(f"Pripojil sa klient: {client_address}")

while True:
    message = client_socket.recv(1024).decode()
    print(f"Správa od klienta: {message}")

    chat_server = input("Zadejte vaši zprávu: ")
    client_socket.sendall(chat_server.encode())



# ip v4 127.0.0.1
import socket
import threading

clients = []
usernames = {}
db = {
    "user1": "pass1",
    "user2": "pass2"
}

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except:
            client_socket.close()
            clients.remove(client_socket)
            break


def receive_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Připojení od {client_address} bylo navázáno.")

        client_socket.send("USERNAME".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')

        client_socket.send("PASSWORD".encode('utf-8'))
        password = client_socket.recv(1024).decode('utf-8')

        if username in db and db[username] == password:
            usernames[client_socket] = username
            clients.append(client_socket)
            print(f"Uživatelské jméno klienta je {username}")
            broadcast(f"{username} se připojil k chatu!".encode('utf-8'), client_socket)
            client_socket.send("Připojení k serveru bylo úspěšné!".encode('utf-8'))

            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()
        else:
            client_socket.send("Neplatné uživatelské jméno nebo heslo.".encode('utf-8'))
            client_socket.send("CLOSE".encode('utf-8'))
            client_socket.close()



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen()

    print("Server naslouchá...")
    receive_connections(server_socket)


if __name__ == "__main__":
    start_server()
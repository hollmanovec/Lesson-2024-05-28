import socket
import threading

rooms = {}
db = {
    "user1": "pass1",
    "user2": "pass2",
    "user3": "pass3",
}


def broadcast(message, room, client_socket):
    """Odošle správu všetkým klientom v miestnosti okrem odosielateľa."""
    for client in rooms[room]:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                rooms[room].remove(client)
                if not rooms[room]:
                    del rooms[room]


def handle_client(client_socket, room):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, room, client_socket)
        except:
            client_socket.close()
            rooms[room].remove(client_socket)
            if not rooms[room]:
                del rooms[room]
            break


def receive_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Připojení od {client_address} bylo navázáno.")

        username, password = client_socket.recv(1024).decode('utf-8').split(":")

        if username in db and db[username] == password:
            client_socket.send("Připojení k serveru bylo úspěšné!".encode('utf-8'))

            print(f"Uživatelské jméno klienta je {username}")
            room = client_socket.recv(1024).decode('utf-8')
            if room not in rooms:
                rooms[room] = []
            rooms[room].append(client_socket)
            print(f"Klient sa pripojil do miestnosti: {room}")

            broadcast(f"{username} se připojil k chatu!".encode('utf-8'),
                      room,
                      client_socket)

            thread = threading.Thread(target=handle_client, args=(client_socket, room))
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
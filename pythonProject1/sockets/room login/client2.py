import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "USERNAME":
                client_socket.send(username.encode('utf-8'))
            elif message == "PASSWORD":
                client_socket.send(password.encode('utf-8'))
            elif message == "CLOSE":
                client_socket.close()
            else:
                print(message)
        except:
            print("Došlo k chybě!")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = f"{username}: {input('zadej spravu: ')}"
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    username = input("Zadejte své uživatelské jméno: ")
    password = input("Zadejte své heslo: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()
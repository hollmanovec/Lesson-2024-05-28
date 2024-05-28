import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12346))

while True:
    chat_client = input("zadejte svou zprávu: ")

    client_socket.sendall(chat_client.encode())
    response = client_socket.recv(1024).decode()
    print(f"Odpoveď zo servera: {response}")


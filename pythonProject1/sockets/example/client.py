import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12346))

client_socket.sendall("Ahoj, server!".encode())
response = client_socket.recv(1024).decode()
print(f"Odpoveď zo servera: {response}")

client_socket.close()
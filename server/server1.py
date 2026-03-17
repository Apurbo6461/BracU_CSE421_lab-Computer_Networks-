import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5050))
server.listen(1)

print("Server is listening...")

conn, addr = server.accept()
print("Connected by:", addr)

data = conn.recv(1024).decode()
print("Client Info:", data)

conn.close()
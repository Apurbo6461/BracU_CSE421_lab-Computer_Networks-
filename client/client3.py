import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5052))

message = input("Enter message: ")
client.send(message.encode())

response = client.recv(1024).decode()
print("Server says:", response)

client.close()
import socket
import platform

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5050))

device_name = platform.node()
ip = socket.gethostbyname(socket.gethostname())

message = f"IP: {ip}, Device: {device_name}"
client.send(message.encode())

client.close()
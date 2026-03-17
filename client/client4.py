import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5053))

hours = input("Enter working hours: ")
client.send(hours.encode())

salary = client.recv(1024).decode()
print("Calculated Salary:", salary)

client.close()
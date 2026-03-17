import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5053))
server.listen(1)

print("Salary server running...")

while True:
    conn, addr = server.accept()
    print("Connected by:", addr)

    hours = float(conn.recv(1024).decode())

    if hours <= 40:
        salary = hours * 200
    else:
        salary = 8000 + (hours - 40) * 300

    conn.send(str(salary).encode())
    conn.close()
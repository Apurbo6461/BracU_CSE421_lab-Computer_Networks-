import socket
import threading

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def handle_client(conn, addr):
    print(f"Connected: {addr}")
    
    msg = conn.recv(1024).decode()
    vowel_count = count_vowels(msg)

    if vowel_count == 0:
        response = "Not enough vowels"
    elif vowel_count <= 2:
        response = "Enough vowels I guess"
    else:
        response = "Too many vowels"

    conn.send(response.encode())
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5052))
server.listen(5)

print("Multi-threaded server running...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
import socket

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5051))
server.listen(1)

print("Server is listening...")

conn, addr = server.accept()
print("Connected by:", addr)

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
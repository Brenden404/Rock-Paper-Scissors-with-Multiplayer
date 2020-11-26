import socket

HOST = "127.0.0.1"
PORT = 65432
print(HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        client_input = input()
        s.send(client_input.encode())
        data = s.recv(1024)
        print('Server:', repr(data.decode()))

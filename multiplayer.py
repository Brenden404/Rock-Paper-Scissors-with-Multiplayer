import socket
import rps


def host():
    HOST = ''
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"A player has connected to your session: {addr}")
            while True:
                print("Starting new game. Please select Rock, Paper, or Scissors by typing '1', '2', or '3'")
                host_choice = int(input())
                host_message = """The host has made their choice. Please select Rock, Paper, or Scissors by typing 
'1', '2', or '3'"""
                conn.sendall(host_message.encode())
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    continue
                client_choice = int(data)
                result = rps.rock_paper_scissors_result(host_choice, client_choice)
                conn.sendall(result.encode())
                break


def join():
    HOST = input()
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to host {HOST} via port {PORT}.")

        while True:
            print("Starting new game. Waiting on Host.")
            data = s.recv(1024)
            if not data:
                continue
            print(data.decode('utf-8'))
            client_choice = input()
            s.sendall(client_choice.encode())
            result = s.recv(1024).decode('utf-8')
            if not result:
                continue

            if result == "win":
                print("You Lose!")
                break

            elif result == "tie":
                print("Tie!")
                break

            elif result == "lose":
                print("You win!")
                break

            else:
                print("Error occurred. Exiting.")
                break

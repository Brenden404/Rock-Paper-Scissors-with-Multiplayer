import random
import multiplayer
import rps
from requests import get


while True:
    print("""Welcome to Rock Paper Scissors! Please select an option by typing '1' or '2':
1) Play a game
2) Quit)""")
    play_game = input()
    if play_game == "1":
        print("""Which gametype would you like to play? Please select an option by typing '1' or '2':
1) Player VS Computer
2) Player VS Player""")
        gametype = input()
        if gametype == "1":
            while True:
                print("Would you like to start a new game? Please type y or n.")
                new_game = input()
                if new_game == "y":
                    print("Starting new game. Please select Rock, Paper, or Scissors by typing '1', '2', or '3'")
                    p_choice = int(input())
                    o_choice = random.randint(1, 3)
                    rps.rock_paper_scissors_result(p_choice, o_choice)

                elif new_game == "n":
                    print("Returning to Main Menu.")
                    break

                else:
                    print("Invalid input")
                    continue

        elif gametype == "2":
            print("""Would you like to host a game or join a game? Please select an option by typing 1 or 2:
1) Host a game
2) Join a game""")
            host_or_join = input()
            if host_or_join == "1":
                ip = get('https://api.ipify.org').text
                print(f"Hosting game with public IP Address {ip}. Waiting on a player to connect:")
                multiplayer.host()
                break

            elif host_or_join == "2":
                print("""Please enter the public IP address of the host you are trying to connect to. Enter the private
IP address of the host you are trying to connect to if connecting over a LAN. Enter 127.0.0.1 if you want to connect
to a game you are hosting on the same computer.""")
                multiplayer.join()
                break

            else:
                print("You have not entered a valid number.")
                continue

        else:
            print("You have not entered a valid number.")
            continue

    elif play_game == "2":
        print("Exiting Rock, Paper, Scissors game")
        break

    else:
        print("Invalid input detected.")
        continue

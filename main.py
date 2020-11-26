import random
from requests import get

def rock_paper_scissors():
    while True:
        print("Would you like to start a new game? Please type y or n.")
        player_yes_no = input()
        try:
            if player_yes_no == "y":
                print("Starting new game. Please select Rock, Paper, or Scissors by typing '1', '2', or '3'")
                player_choice = int(input())
                opponent_choice = random.randint(1, 3)
                opponent_rock = "Opponent has selected Rock."
                opponent_paper = "Opponent has selected Paper."
                opponent_scissors = "Opponent has selected Scissors."
                if player_choice == 1 and opponent_choice == 1:
                    print(f"{opponent_rock} You tied.")

                elif player_choice == 1 and opponent_choice == 2:
                    print(f"{opponent_paper} Computer wins :(")

                elif player_choice == 1 and opponent_choice == 3:
                    print(f"{opponent_scissors} You win!")

                elif player_choice == 2 and opponent_choice == 1:
                    print(f"{opponent_rock} You win!")

                elif player_choice == 2 and opponent_choice == 2:
                    print(f"{opponent_paper} You tied.")

                elif player_choice == 2 and opponent_choice == 3:
                    print(f"{opponent_scissors} Computer wins :(")

                elif player_choice == 3 and opponent_choice == 1:
                    print(f"{opponent_rock} Computer wins :(")

                elif player_choice == 3 and opponent_choice == 2:
                    print(f"{opponent_paper} You win!")

                elif player_choice == 3 and opponent_choice == 3:
                    print(f"{opponent_scissors} You tied.")

                else:
                    print("You have not entered a valid number.")
                    continue

            elif player_yes_no == "n":
                print("Returning to Main Menu.")
                break

            else:
                raise ValueError

        except ValueError:
            print("You have not entered a valid number.")
            continue


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
            rock_paper_scissors()

        elif gametype == "2":
            print("""Would you like to host a game or join a game? Please select an option by typing 1 or 2:
            1) Host a game
            2) Join a game""")
            host_or_join = input()
            if host_or_join == "1":
                ip = get('https://api.ipify.org').text
                print(f"Hosting game with public IP Address {ip}.")

            elif host_or_join == "2":
                print("Please enter the public IP address of the host you are trying to connect to.")

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

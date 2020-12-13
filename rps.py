def rock_paper_scissors_result(player_choice, opponent_choice):
    try:
        opponent_rock = "Opponent has selected Rock."
        opponent_paper = "Opponent has selected Paper."
        opponent_scissors = "Opponent has selected Scissors."
        if player_choice == 1 and opponent_choice == 1:
            print(f"{opponent_rock} You tied.")
            return "tie"

        elif player_choice == 1 and opponent_choice == 2:
            print(f"{opponent_paper} Opponent wins :(")
            return "win"

        elif player_choice == 1 and opponent_choice == 3:
            print(f"{opponent_scissors} You win!")
            return "lose"

        elif player_choice == 2 and opponent_choice == 1:
            print(f"{opponent_rock} You win!")
            return "lose"

        elif player_choice == 2 and opponent_choice == 2:
            print(f"{opponent_paper} You tied.")
            return "tie"

        elif player_choice == 2 and opponent_choice == 3:
            print(f"{opponent_scissors} Opponent wins :(")
            return "win"

        elif player_choice == 3 and opponent_choice == 1:
            print(f"{opponent_rock} Opponent wins :(")
            return "win"

        elif player_choice == 3 and opponent_choice == 2:
            print(f"{opponent_paper} You win!")
            return "lose"

        elif player_choice == 3 and opponent_choice == 3:
            print(f"{opponent_scissors} You tied.")
            return "tie"

        else:
            print("You have not entered a valid number.")
            raise ValueError

    except ValueError:
        print("You have not entered a valid number.")
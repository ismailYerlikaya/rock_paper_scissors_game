import random


def rock_paper_scissors_ismail_yerlikaya():
    items = ["Rock", "Paper", "Scissors"]
    game = 0
    round_number = 0
    computer_wins = 0
    human_wins = 0
    computer_choices = ["Yes", "No"]

    def rock_paper_scissors():

        nonlocal game, round_number, computer_wins, human_wins
        game += 1
        round_number += 1
        while True:
            print(f"GAME {game}. ROUND {round_number} STARTING")
            print("Please choose one (Rock, Paper, Scissors):")
            human_choice = input()
            computer_choice = random.choice(items)

            while human_choice not in items:
                print("Invalid choice, please choose again (Rock, Paper, Scissors):")
                human_choice = input()

            if (human_choice == "Rock" and computer_choice == "Paper") or \
               (human_choice == "Paper" and computer_choice == "Scissors") or \
               (human_choice == "Scissors" and computer_choice == "Rock"):
                computer_wins += 1
                print(f"Computer won round {round_number}")
                round_number += 1

            elif (human_choice == "Paper" and computer_choice == "Rock") or \
                 (human_choice == "Scissors" and computer_choice == "Paper") or \
                 (human_choice == "Rock" and computer_choice == "Scissors"):
                human_wins += 1
                print(f"Human won round {round_number}")
                round_number += 1

            else:
                print("No winner, this round is a draw")
                round_number += 1

            print(f"Computer's choice: {computer_choice}")
            print(f"Computer = {computer_wins}, Human = {human_wins}")
            print("////////////////////////////////////////////////////////////////")

            if human_wins == 2:
                print("Human won the game!")
                print("Congratulations, very few people have beaten the computer so far.")
                round_number = 0
                human_wins = 0
                break
            elif computer_wins == 2:
                print("Computer won the game!")
                round_number = 0
                computer_wins = 0
                break
    print("##############################################################################################")
    print("Hello, are you ready to play Rock Paper Scissors?")
    print("""Game Rules: Rock Paper Scissors is a simple game.
    If the computer chooses rock and you choose paper, paper covers rock and you win.
    If you choose scissors and the computer chooses rock, you lose. In summary, paper beats rock, rock beats scissors,
    and scissors beat paper.
    If a player wins 2 rounds, they win the game.""")
    print("""    History of the Game: The "Rock, Paper, Scissors" game originated in ancient China under the name "Shoushiling."
    Played during the Han Dynasty period between 206-220 BC, it traveled to Japan where it became known as "Jan-Ken."
    From there, it spread worldwide. Today, this simple hand game is known and played globally.""")
    print("#################################################################################################")
    print("Now that you know the game rules, are you ready to play? (Yes/No)")
    human_wants_to_play = input()

    computer_wants_to_play = "Yes"

    while human_wants_to_play not in ["Yes", "No"]:
        print("You entered an incorrect response")
        print("Do you want to play (Yes/No)?")
        human_wants_to_play = input()

    while True:
        if human_wants_to_play == "Yes" and computer_wants_to_play == "Yes":
            rock_paper_scissors()
            print("Do you want to play again? (Yes/No)")
            human_wants_to_play = input()
            while human_wants_to_play not in ["Yes", "No"]:
                print("You entered an incorrect response")
                print("Do you want to play (Yes/No)?")
                human_wants_to_play = input()
            computer_wants_to_play = random.choice(computer_choices)

        elif computer_wants_to_play == "No" and human_wants_to_play == "Yes":
            print(f"Human = {human_wants_to_play}, Computer = {computer_wants_to_play}")
            print("Computer:I know you want to play, but my mom is calling me home, I need to go.")
            break

        elif human_wants_to_play == "No" and game == 0:
            print("OOOOOOPPPPPPSSSSS! Where are you going before the game has even started?")
            print("Are you sure you want to exit? (Yes/No)")
            human_wants_to_play = input()
            while human_wants_to_play not in ["Yes", "No"]:
                print("You entered an incorrect response")
                print("Do you want to exit the game? (Yes/No)")
                human_wants_to_play = input()
            if human_wants_to_play == "Yes":
                break
            else:
                rock_paper_scissors()
                print("Do you want to play again? (Yes/No)")
                human_wants_to_play = input()
                while human_wants_to_play not in ["Yes", "No"]:
                    print("You entered an incorrect response")
                    print("Do you want to play (Yes/No)?")
                    human_wants_to_play = input()
                computer_wants_to_play = random.choice(computer_choices)
                if computer_wants_to_play == "No" and human_wants_to_play == "Yes":
                    print(f"Human = {human_wants_to_play}, Computer = {computer_wants_to_play}")
                    print("Computer:I know you want to play, but my mom is calling me home, I need to go.")
                    break

        elif human_wants_to_play == "No":
            print("We played a little, but if you don't want to play, it's up to you.")
            break

    print("THE GAME IS OVER")


rock_paper_scissors_ismail_yerlikaya()

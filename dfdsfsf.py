import random

def convert_userInput(computer_choice):
    if computer_choice == "1":
        computer_choice = "foot"
    elif computer_choice == "2":
        computer_choice = "nuke"
    else:
        computer_choice = "cockroach"

    return computer_choice

def game_logig(PC, CC , player_score , round_played , ties):
    round_played += 1
    if PC == "Foot" and CC == "cockroach":
        print("You WIN!")
        player_score += 1
    elif PC == "nuke" and CC == "foot":
        print("You WIN!")
        player_score += 1
    elif PC == "cockroach" and CC == "nuke":
        print("You WIN!")
        player_score += 1
    elif PC == CC == "nuke":
        print("Both LOSE!")
    elif PC == CC:
        print("It is a tie!")
        ties += 1
    else:
        print("You LOSE!")
    return player_score,round_played,ties

def nuke_foot_cockroach():
    player_score = 0
    ties = 0
    rounds_played = 0
    while True:
        player_choice = input("Foot, Nuke or Cockroach? (Quit ends): ")

        if player_choice == 'Quit':
            print(f"You played {rounds_played} rounds, and won {player_score} rounds,playing  tie in {ties} rounds.")
            break

        print(f"You chose: {player_choice}")
        computer_choice = str(random.randint(1, 3))

        computer_choice = convert_userInput(computer_choice)
        print(f"Computer chose: {computer_choice}")

        player_score ,rounds_played,ties  =  game_logig(player_choice.lower(),computer_choice , player_score, rounds_played,ties)


nuke_foot_cockroach()

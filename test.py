import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None


    while player not in choices:
        player = input("rock,paper,scissors?: ")

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":#
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You winn!")
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
    elif player == "paper":#
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You winn!")
    elif player == "scissors":#
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You winn!")    


    play_again = input("Wanna play again? (yes/no): ")

    if play_again != "yes":
        print("Bye :)")
        break

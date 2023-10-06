import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper, or scissors?: ").lower()

    if player == computer:
        print("Player: "+player)
        print("Computer: "+computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Player: "+player)
            print("Computer: "+computer)
            print("You lose!")
        if computer == "scissors":
            print("Player: "+player)
            print("Computer: "+computer)
            print("You winn!")
    elif player == "paper":
        if computer == "rock":
            print("Player: "+player)
            print("Computer: "+computer)
            print("You winn!")
        if computer == "scissors":
            print("Player: "+player)
            print("Computer: "+computer)
            print("You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("Player: "+player)
            print("Computer: "+computer)
            print("You winn!")
        if computer == "rock":
            print("Player: "+player)
            print("Computer: "+computer)
            print("You lose!")
    if player != computer:
        again = input("Do ypou wanna play again? (yes/no): ")
        if again != "yes":
            break
print("Bye! :)")
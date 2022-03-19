import random

# function to randomly choose between rock paper and scissors
def choose_rps():
    # output: randomly returns rock, paper, or scissors
    options = ["rock", "paper", "scissors"]
    return options[random.randint(0,2)]

# output: prints the winner of the game
def rps(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 won!")
        else:
            print("Player 2 won!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 won!")
        else:
            print("Player 2 won!")

play = "yes"
while play == "yes":
    # game greeting
    print("Welcome to Rock, Paper, Scissors!")
    print("-----")

    # ask player1 and player2 to input their rps choice
    player1_choice = input("Player 1: do you choose rock, paper, or scissors?")
    player2_choice = input("Player 2: do you choose rock, paper, or scissors?")
    print("-----")

    # print player1 and player2's choice
    print("Player 1 chose " + player1_choice)
    print("Player 2 chose " + player2_choice)
    print("-----")

    # print the winner of the game
    rps(player1_choice, player2_choice)

    # ask user if they'd like to play again
    play = input("Would you like to play again? (yes or no)")
    
print("Thank you for playing!")
    

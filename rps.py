import random

# function prompting player to choose between rock paper or scissors
def player_rps():
    while True:    
        print("Do you choose rock, paper, or scissors?")
        player_choice = input()
        player_choice = player_choice.lower()
        if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
            print("Please choose between: rock, paper, scissors")     
        else:
            return player_choice 

# function randomly selecting a choice for the computer
def computer_rps():
    options = ["rock", "paper", "scissors"]
    computer_choice = options[random.randint(0, 2)]
    return computer_choice
    
# output: prints the winner of the game
def rps(player, computer):
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You won! Congrats!")
        else:
            print("The computer won :(")
    elif player == "paper":
        if computer == "rock":
            print("You won! Congrats!")
        else:
            print("The computer won :(")
    elif player == "scissors":
        if computer == "paper":
            print("You won! Congrats!")
        else:
            print("The computer won :(")

play = "yes"
while play == "yes":
    # game greeting
    print("Welcome to Rock, Paper, Scissors!")

    # ask player to input their rps choice
    player = player_rps()
   
    # computer randomly chooses
    computer = computer_rps()
    print("-----")

    # print the results of the game
    print("You chose: " + player.upper())
    print("The computer chose: " + computer.upper())
    print("-----")
    rps(player, computer)

    # ask user if they'd like to play again
    play = input("Would you like to play again? (yes or no)")
    print("-----")

print("Thank you for playing!")
    

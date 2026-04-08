import random

def start():
    rps = "rock","paper","scissors"
    computer = random.choice(rps)

    player = input("Rock,Paper or Scissors?: ")
    player.lower()

    print("Computer: "+computer)
    print("Player: "+player)
    result(computer, player)

    game = input("Play again? YES/NO: ")
    play_again(game)
def result(computer,player):
    if computer == player:
        print("Tie!")

    if player == "rock" and computer == "scissors":
        print("You win!")

    if player == "scissors" and computer == "rock":
        print("You lose!")

    if player == "rock" and computer == "paper":
        print("You lose!")

    if player == "paper" and computer == "scissors":
        print("You lose!")

    if player == "scissors" and computer == "paper":
        print("You win!")

    if player == "paper" and computer == "rock":
        print("You win!")


def play_again(game):
    game.lower()
    if game == "yes":
        start()
    else:
        print("Good Game Bye!")
        #clear_console()
        exit()

start()








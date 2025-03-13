import random
print("----------------------------------------")
print("Welcome To The Rock Paper Scissors Game")
print("----------------------------------------")
name = input("What is Your name : ")


while True:
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)

    player = input("Enter Rock , Paper Or Scissors : ").lower()

    width = 10

    print(f"{name:<{width}} : {player.capitalize()}")
    print(f"{'Computer':<{width}} : {computer.capitalize()}")
    if player == "rock" and computer == "scissors":
        print("You Won!")
    elif player == "paper" and computer == "rock":
        print("You Won!")
    elif player == "scissors" and computer == "paper":
        print("You Won!")
    elif {player} == {computer}:
        print("Please Try Again!")
        continue
    else:
        print("You Lost!")


    is_playing=input("Do You want to Play Again (Y/N) : ").lower()
    if is_playing == "n" :
        print("Thank You For Playing!")
        break





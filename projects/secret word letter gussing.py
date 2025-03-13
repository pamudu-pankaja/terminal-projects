while True:
    word = "HOPPERS"

    letter = input("Enter A letter : ").capitalize()

    if letter in word:
        print(f"You won There is {letter} ")
    else:
        print(f"There isn't {letter} in the word you lost")

    is_playing= input("Do you want to play again (Enter Y/N) : ").lower()
    if is_playing=="n":
        break





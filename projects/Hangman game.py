import random

words = ["apple","pineapple","banana","grapes","strawberries","orange"]

hangman_stages = {
    0: """
------
|    |
|
|
|
|
--------
""",
    1: """
------
|    |
|    O
|
|
|
--------
""",
    2: """
------
|    |
|    O
|    |
|
|
--------
""",
    3: """
------
|    |
|    O
|   /|
|
|
--------
""",
    4: """
------
|    |
|    O
|   /|\\
|
|
--------
""",
    5: """
------
|    |
|    O
|   /|\\
|   /
|
--------
""",
    6: """
------
|    |
|    O
|   /|\\
|   / \\
|
--------
"""
}


def print_hangman(wrong_guesses):
    print("**************")
    print(hangman_stages[wrong_guesses])
    print("**************")

def print_hint(hint):

    print(" ".join(hint))

def print_answer(answer):
    print(" ".join(answer),)
    print("| Is the correct answer")
    print("**************")

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses= 0
    guessed_letters= set()
    is_running = True

    while is_running:
        print_hangman(wrong_guesses)
        print_hint(hint)
        guess = input("Enter a letter : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        else:
            guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i]= guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            print_hangman(wrong_guesses)
            print_answer(answer)
            print("| You Won!")
            is_running = False
        elif wrong_guesses >= len(hangman_stages) -1:
            print_hangman(wrong_guesses)
            print_answer(answer)
            print("| You Lose!")
            is_running = False
if __name__ == "__main__":
    main()




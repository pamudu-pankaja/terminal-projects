questions = ("What is the best game : ",
             "Who did best : ",
             "Who we vote for :")
options = (("A. Valorant", "B. Minecraft", "C. Blood strike"),
           ("A. Gotabaya", "B. Ubett", "C. Mahinda mahaththaya"),
           ("A. Namal ", "B. Anura", "C. Sajiya"))

answers = ("A", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    while True:
        print("-----------------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C): ").upper()

        if guess == "":
            print("-----------------------------")
            print("Please enter an answer")
        elif guess in ['A', 'B', 'C']:
            break
        else:
            print("-----------------------------")
            print("Invalid input. Please enter A, B, or C.")

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("-----------------")
print("-----Results-----")
print("-----------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print("-----------------")
if score > 0:
    print(f"You got {score}/{len(questions)} of the questions right")
else:
    print("You got none of the questions right")

print("-----------------")

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
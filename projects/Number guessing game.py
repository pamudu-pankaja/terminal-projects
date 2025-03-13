import random

def get_range():
    while True:
        user_range=input("Enter a range (N to exit) : ").lower()
        if user_range.strip()=="":
            print("Please enter a range")
        elif user_range=="n":
            print("--------------------")
            print("|Thank you,Have a nice day!")
            return "exit"
        else:
            try:
                user_range=int(user_range)
                if user_range==0:
                    print("Enter a range greater than ZERO")
                else:
                    return user_range
            except ValueError:
                print("--------------------")
                print("Please Enter a range")


def get_number(top_number,right_guess):
    while True:
        print("--------------------")
        print(f"Your range is 0-{top_number}")
        print("------------------------")
        user_number=input("Enter a number (N to exit) : ").lower()
        if user_number.strip()=="":
            print("Please enter a number")
        elif user_number=="n":
            print("--------------------")
            print("|Thank you,Have a nice day!")
            print(f"|You have won {right_guess} guesses")
            return "exit"
        else:
            try:
                user_number=int(user_number)
                if user_number < 0:
                    print("Invalid input")
                    return "again"
                elif user_number>top_number:
                    print("Invalid input")
                    return "again"
                else:
                    return user_number
            except ValueError:
                print("--------------------")
                print("Please Enter a number")

def main():
    right_guess=0
    is_running=True
    top_number = get_range()

    while is_running:
        guess = get_number(top_number,right_guess)
        if guess == "exit":
            is_running=False
        elif guess=="again":
            continue
        else:
            random_num = random.randint(0,top_number)
            if random_num== guess:
                print("*****************")
                print("You won!")
                print("*****************")
                right_guess+=1
            else:
                print("--------------------")
                print("You Lost!")
                print(f"{random_num} is the random number")


if __name__=="__main__":
    main()






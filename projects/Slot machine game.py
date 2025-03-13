import random

def symbol_row():
    symbols = ["🍒",
               "🍉",
               "🥭",
               "🔔",
               "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row, ):
    print(" | ".join(row))
    print("---------------------------------")

def get_payout(row, bet):

    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🥭":
            return bet * 4
        elif row[0] == "🔔":
            return  bet * 5
        elif row[0] == "⭐":
            return bet * 10

    return 0

def main():
    balance = 0

    print("---------------------------------")
    print("Welcome to the Python Slot Game")
    print("Symbols : 🍒 | 🍉 | 🥭 | 🔔 | ⭐")
    print("---------------------------------")


    while True:
        money = float(input("How much would you like to enter ($): "))
        if money > 0:
            balance += money
            break
        elif money <= 0:
            print("You must enter more than 0 dollars.")
            x = input("Would you like to add more money and play? (Y/N): ").upper()
            if x != "Y":
                print("Thank you, have a nice day!")
                return

    while balance > 0:
        print("---------------------------------")
        bet = float(input("How much would you like to bet ($): "))
        if balance < bet:
            print("Insufficient Funds")
        else:
            balance -= bet
            row = symbol_row()
            print("---------------------------------")
            print("Spinning...\n")
            print_row(row, )


            payout = get_payout(row, bet)
            if payout > 0:
                balance += payout
                print(f"Congratulations! You won ${payout}!")
                print("---------------------------------")
                print(f"Your current balance is ${balance}")
            else:
                print("Sorry, you didn't win this time.")
                print("---------------------------------")
                print(f"Your current balance is ${balance}")


            if balance > 0:
                x = input("Do you want to bet again? (Y/N): ").upper()
                if x != "Y":
                    print("Thank you for playing! Goodbye!")
                    print(f"You have won ${balance}")
                    break
            else:
                print("You have run out of money. Game over!")
                print(f"You have won ${balance}")

if __name__ == "__main__":
    main()

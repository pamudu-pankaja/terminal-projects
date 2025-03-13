import random


def spinning_row():
    symbols = ["🍒", "🍉", "🥭", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))
    print("---------------------------------")


def get_payout(row, bet1):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet1 * 2
        elif row[0] == "🍉":
            return bet1 * 3
        elif row[0] == "🥭":
            return bet1 * 4
        elif row[0] == "🔔":
            return bet1 * 5
        elif row[0] == "⭐":
            return bet1 * 10
    return 0


def get_bet(balance, first_round=False):
    while True:
        if first_round:
            bet = input("Enter your bet: ")
        else:
            bet = input("Enter your bet (or 'N' to exit): ").upper()

        if bet == "N" and not first_round:
            return "N"

        try:
            bet = float(bet)
            if bet <= 0:
                print("Invalid bet. Please enter a positive amount.")
            elif bet > balance:
                print("Insufficient funds.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a number or 'N' to exit ")


def play_round(balance):
    first_round = True

    while balance > 0:
        bet1 = get_bet(balance, first_round)

        if bet1 == "N":
            print("Thank you for playing!")
            break

        row = spinning_row()
        balance -= bet1

        print("---------------------------------")
        print("Spinning...\n ")
        print_row(row)

        payout = get_payout(row, bet1)

        if payout > 0:
            balance += payout
            print(f"You have won ${payout:.2f}")
        else:
            print("You have lost this round")

        print("---------------------------------")
        print(f"Your current balance is ${balance:.2f}")

        if balance <= 0:
            print("You have run out of funds. Thank you for playing!")
            break


        first_round = False


def main():
    print("---------------------------------")
    print("Welcome to the Python Slot Game")
    print("Symbols : 🍒 | 🍉 | 🥭 | 🔔 | ⭐")
    print("---------------------------------")

    while True:
        balance = float(input("How much would you like to enter ($): "))
        if balance <= 0:
            print("You must enter more than 0 dollars.")
            again = input("Do you want to play or exit (Y/N): ").upper()
            if again == "N":
                print("Thank you, have a nice day.")
                break
        else:
            play_round(balance)
            break


if __name__ == "__main__":
    main()

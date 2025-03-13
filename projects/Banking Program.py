

def show_balance(balance):
    print("*********************")
    print(f"Your balance is Rs.{balance:.2f}")


def deposit():
    print("*********************")
    amount = float(input("How much Would You like to deposit (Rs.) : "))


    if amount < 0 :
        print("*********************")
        print("That is not a valid amount")

        return 0
    else :
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("How much Would You like to withdraw (Rs.) : "))


    if amount > balance :
        print("*********************")
        print("You don't have that much money in this account ")
        return 0
    elif amount < 0:
        print("*********************")
        print("That is Not a Valid Amount")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True
    while is_running:
        print("*********************")
        print("-----Bank Program----")
        print("*********************")
        print("1.Check the Balance")
        print("2.Make a Deposit")
        print("3.Make a Withdrawal")
        print("4.Exit")
        choice=int(input("What do You want to do Today (1-4): "))


        if choice == 1:
            show_balance(balance)

        elif choice == 2:
            balance += deposit()

        elif choice == 3:
            balance -= withdraw(balance)

        elif choice == 4:
            is_running = False
            print("Thank You, Have a nice day!")
        else:
            print("That is not a valid Choice")


if __name__ == "__main__":
    main()











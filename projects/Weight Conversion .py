weight = float(input("Enter your weight : "))
answer = input("Is this Kilograms or Pounds (K/L) ?: ")

if answer == "K":
    weight = weight * 2.205
    answer = "Lbs."
    print(f"Your weight is : {round(weight,1)} {answer} ")
elif answer == "L":
    weight = weight / 2.205
    answer = "Kgs."
    print(f"Your weight is : {round(weight,1)} {answer} ")
else:
    print(f"{answer} is not valid")





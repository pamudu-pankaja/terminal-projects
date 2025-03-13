

foods = []
prices = []
total = 0

while True :
    food = input("Enter your food (q to quit) : ")
    if food.lower() == "q":
        break
    else :
        price = float(input(f"Enter the price of {food} : $" ))
        prices.append(price)
        foods.append(food)

print("------ YOUR CART ------")
print(" ")

max_length= max(len(food) for food in foods)

for food,price in zip(foods,prices) :
    print(f"{food:<{max_length}} : ${price:.2f}")

total=sum(prices)

print(" ")

print(f"Your total will be : ${total:.2f}")
print("Thank You for Shopping with us")







































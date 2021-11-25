# make 3 hot flavours
# espresso, latte, cappuccino

# espresso is $1.50 - 50ml water, 18g coffee
# latte is $2.50 - 200ml water, 24g coffee, 150ml milk
# cappuccino is$3.00 -  250ml water, 24g coffee, 100ml milk

# machine has:
# 300ml water
# 200ml milk
# 100g coffee

# coin operated and 4 types of coins
# "Penny" is 1 cent $0.01
# "Nickel" is 5 cents $0.05
# "Dime" is 10 cents $ 0.10
# "Quarter" is 25 cents $0.25

# TODO:
# 1 - Print report
# 2 - Check resources sufficient?
# 3 - Process coins
# 4 - Ask for different types of coin
# 5 - If not enough money, refund
# 6 - If enough, calculate the price and change
# 7 - Check if transaction is successful
# 8 - Make coffee and deduct resources


from  coffeeData import MENU
from coffeeData import resources


def coffeeMachine():
    continues = True
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources ["coffee"]
    money = 0
    sales = 0
    while continues:
        question = input("What would you like? Espresso, Latte or Cappuccino? ").lower()
        milkNeeded = 0
        if question == "cappucino":
            question = "cappuccino"
        if question == "report":
            print("")
            print(f"Water {water}ml")
            print(f"Milk {milk}ml")
            print(f"Coffee {coffee}g")
            print(f"Money ${money}")
            print(f"Number of sales {sales}")
            milkNeeded = 0
            waterNeeded = 0
            coffeeNeeded = 0
            continues = False
            break
        elif question == "espresso":
            waterNeeded = MENU["espresso"]["ingredients"]["water"]
            coffeeNeeded = MENU["espresso"]["ingredients"]["coffee"]
            price = 1.50
        elif question == "latte":
            waterNeeded = MENU["latte"]["ingredients"]["water"]
            coffeeNeeded = MENU["latte"]["ingredients"]["coffee"]
            milkNeeded = MENU["latte"]["ingredients"]["milk"]
            price = 2.50
        elif question == "cappuccino":
            waterNeeded = MENU["cappuccino"]["ingredients"]["water"]
            coffeeNeeded = MENU["cappuccino"]["ingredients"]["coffee"]
            milkNeeded = MENU["cappuccino"]["ingredients"]["milk"]
            price = 3.00
        water -= waterNeeded
        coffee -= coffeeNeeded
        milk -= milkNeeded
        penny = float(input("How many pennies?    ")) * 0.01
        nickel = float(input("How many nickels?    ")) * 0.05
        dime = float(input("How many dimes?    "))  * 0.10
        quarter = float(input("How many quarters?    ")) * 0.25
        userMoney = penny + nickel + dime + quarter
        if userMoney >= price:
            change = userMoney - price
            print ("Transaction successful!")
        elif userMoney < price:
            print (f"Sorry not enough money. You need ${round((price - userMoney),2)} more.")
        elif waterNeeded > water:
            print ("Not enough water, sorry!")
        elif coffeeNeeded > coffee:
            print ("Not enough coffee, sorry!")
        elif milkNeeded > milk:
            print ("Not enough milk, sorry!")
        if change > 0:
            print(f"Here's your change, ${change}")
        print(f"Enjoy your {question.title()}!")
        sales += 1
        money += price
        if input("Would you like to order again? 'y' or 'n'") == "n":
            print("Have a nice day!")
            continues = False


coffeeMachine()


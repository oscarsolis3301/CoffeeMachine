def report(remaining_water, remaining_milk, remaining_coffee, money_total):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def check_coins(choice, price):
    user_quarters = float(input(f"How many quarters?: "))
    user_dimes = float(input(f"How many dimes?: "))
    user_nickles = float(input(f"How many nickles?: "))
    user_pennies = float(input(f"How many pennies?: "))

    user_coin_amount = (.25 * user_quarters) + (.10 * user_dimes) + (.05 * user_nickles) + (.01 * user_pennies)

    if user_coin_amount < price:
        return False
    elif user_coin_amount >= price:
        change = user_coin_amount - price
        print(f"Here is ${change} in change.")


water = 300
milk = 200
coffee = 100
money = 0

stopped = False
while not stopped:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    coffee_choice = str(input("What would you like? (espresso/latte/cappuccino): "))
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if coffee_choice == "off":
        print("Please come again soon.")
        print("Goodbye!")
        stopped = True
    elif coffee_choice == "report":
        report(water, milk, coffee, money)
    elif coffee_choice == "espresso":
        check_coins(coffee_choice, price=2.00)
    elif coffee_choice == "latte":
        check_coins(coffee_choice, price=2.50)
    elif coffee_choice == "cappuccino":
        check_coins(coffee_choice, price=3.00)
# TODO 3. Print report.

# TODO 4. Check resources sufficient?

# TODO 5. Process coins.
coins = {
    ".25": "quarter",
    ".10": "dime",
    ".05": "nickel",
    ".01": "pennies",
}

# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.

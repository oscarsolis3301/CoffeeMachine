from data import resources, coffee


def report(remaining_water, remaining_milk, remaining_coffee, money_total):
    print(f"Water: {remaining_water}ml")
    print(f"Milk: {remaining_milk}ml")
    print(f"Coffee: {remaining_coffee}g")
    print(f"Money: ${money_total}")


def check_balance(choice, price):
    user_quarters = .25 * float(input(f"How many quarters?: "))
    user_dimes = .1 * float(input(f"How many dimes?: "))
    user_nickles = .05 * float(input(f"How many nickles?: "))
    user_pennies = .01 * float(input(f"How many pennies?: "))
    user_total = user_quarters + user_dimes + user_nickles + user_pennies
    if user_total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif user_total >= price:
        make_coffee(user_total, choice, price)
        return True


def make_coffee(user_money, choice, price):
    change = round(user_money - price, 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {choice} ☕.Enjoy!")


def check_resources(choice):
    if choice in coffee:
        if coffee[choice]["water"] <= resources["water"]:
            if coffee[choice]["milk"] <= resources["milk"]:
                if coffee[choice]["coffee"] <= resources["coffee"]:
                    update_report(choice)
                    return True
                else:
                    print("Sorry there is not enough coffee.")
                    return False
            else:
                print("Sorry there is not enough milk.")
                return False
        else:
            print("Sorry there is not enough water.")
            return False
    else:
        return False


def update_report(choice):
    resources["water"] -= coffee[choice]["water"]
    resources["milk"] -= coffee[choice]["milk"]
    resources["coffee"] -= coffee[choice]["coffee"]
    resources["money"] += coffee[choice]["cost"]


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
        report(resources["water"], resources["milk"], resources["coffee"], resources["money"])
    elif coffee_choice == "espresso":
        enough_resources = check_resources(coffee_choice)
        if enough_resources:
            enough_balance = check_balance(coffee_choice, price=1.50)
        else:
            print(f"Not enough resources to make a {coffee_choice}")
    elif coffee_choice == "latte":
        enough_resources = check_resources(coffee_choice)
        if enough_resources:
            enough_balance = check_balance(coffee_choice, price=2.50)
        else:
            print(f"Not enough resources to make a {coffee_choice}")
    elif coffee_choice == "cappuccino":
        enough_resources = check_resources(coffee_choice)
        if enough_resources:
            enough_balance = check_balance(coffee_choice, price=3.00)
        else:
            print(f"Not enough resources to make {coffee_choice}")
    else:
        coffee_choice = ""
        print("Please enter a proper input.")
# TODO 3. Print report.

# TODO 4. Check resources sufficient?

# TODO 5. Process coins.

# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.

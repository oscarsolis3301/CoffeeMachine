stopped = False
while not stopped:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_input = str(input("What would you like? (espresso/latte/cappuccino): "))
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        print("Please come again soon.")
        print("Goodbye!")

# TODO 3. Print report.
def report (water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}")
# TODO 4. Check resources sufficient?

# TODO 5. Process coins.
coins = {
    ".25": "quarter",
    ".10": "dime",
    ".05": "nickel",
}


# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.

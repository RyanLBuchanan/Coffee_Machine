# Import necessary libraries and resources
from data import emojis, MENU, resources
from colorama import Fore, Style


# TODO add 'profit' to report statement
profit = 0

# TODO add Angela's 'check_resources' function
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f" Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, there is not enough money. Money refunded.")
        return False


def check_resources(user_input):
    """
    Check if there are sufficient resources to make the selected drink.

    Args:
        user_input (str): The selected drink.

    Returns:
        bool: True if there are enough resources, False otherwise.
    """
    # 4. Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
    # resources to make that drink.

    if resources['water'] >= MENU[user_input]['ingredients']['water'] and resources['milk'] >= \
            MENU[user_input]['ingredients']['milk'] and resources['coffee'] >= MENU[user_input]['ingredients'][
        'coffee']:
        return True
    else:
        # TODO if Latte requires 200ml water but there is only 100ml left in the machine. It should
        # not continue to make the drink but print: “Sorry there is not enough water.”
        # c. The same should happen if another resource is depleted, e.g. milk or coffee.
        return False


def order_drink(user_input):
    """
    Order a drink by checking resources and inserting coins.

    Args:
        user_input (str): The selected drink.

    Returns:
        None
    """
    check_resources(user_input)

    insert_coins(user_input)


def insert_coins(user_input):
    """
    Process coins, calculate the monetary value, and check transaction success.

    Args:
        user_input (str): The selected drink.

    Returns:
        None
    """
    # 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should
    # prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    print("Please insert coins.")
    cash = int(input("How many quarters?: ")) * .25
    cash += int(input("How many dimes?: ")) * .10
    cash += int(input("How many nickels?: ")) * .05
    cash += int(input("How many pennies?: ")) * .01

    # return cash

    # 6. Check transaction successful?
    # a. Check that the user has inserted enough money to purchase the drink they selected.
    # if Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    # program should say “Sorry that's not enough money. Money refunded.”.
    # b. But if the user has inserted enough money, then the cost of the drink gets added to the
    # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # c. If the user has inserted too much money, the machine should offer change.
    # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
    # places.
    if cash >= MENU[user_input]["cost"]:
        change = cash - MENU[user_input]["cost"]
        # Format the change amount to display two decimal places
        change_formatted = "${:.2f}".format(change)

        # 7. Make Coffee.
        # a. If the transaction is successful and there are enough resources to make the drink the
        # user selected, then the ingredients to make the drink should be deducted from the
        # coffee machine resources.
        # E.g. report before purchasing latte:
        # Water: 300ml
        # Milk: 200ml
        # Coffee: 100g
        # Money: $0
        # Report after purchasing latte:
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
        # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
        # latte was their choice of drink.
        resources['money'] += MENU[user_input]['cost']
        resources['water'] -= MENU[user_input]['ingredients']['water']
        resources['milk'] -= MENU[user_input]['ingredients']['milk']
        resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
        print(f"Here is ${change_formatted} in change.\nHere is your {user_input} {emojis[user_input]}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

    # 3. Print report.


def print_report():
    """
    Print a report showing the current resource values.

    Args:
        None

    Returns:
        None
    """
    # a. When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values. e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    money_formatted = "${:.2f}".format(resources['money'])
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_formatted}")


is_on = True

# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
while is_on:
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # a. Check the user’s input to decide what to do next.
    choice = input(f" What would you like? (espresso/latte/cappuccino): \n{Fore.RED}Type 'report' for maintenance\n"
                   f"Or 'off' to quit{Style.RESET_ALL}\n").lower()

    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
    # If the desired condition is met, set the is_on to True
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        order_drink(choice)
        # if is_resource_sufficient(choice):
        #     payment = insert_coins(choice)
        #     is_transaction_successful(payment, drink["cost"])

    else:
        print("That is invalid input. Please enter your coffee order.")



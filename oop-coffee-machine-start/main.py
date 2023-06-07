from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from colorama import Fore, Style

my_coffee_machine = CoffeeMaker()

my_money_machine = MoneyMachine()

menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f" What would you like? ({options}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee_machine.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_machine.make_coffee(order=drink)




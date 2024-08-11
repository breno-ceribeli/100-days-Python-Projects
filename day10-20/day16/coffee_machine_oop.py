#Working with "external" libraries exercise
#None of these Classes were made by me
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like ? ({options}): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffe_maker.make_coffee(drink)
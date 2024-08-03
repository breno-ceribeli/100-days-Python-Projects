from data import MENU, resources, money


def show_options(menu):
    """Print the coffee options and their costs with a string formated correctly.

    Args:
        menu (dict): The dictionary that contains only the coffee options (as the keys) that are expected to be shown.
    """
    print("Available coffee options:  ", end="")
    for option in menu:
        print(f"{option.title()} - ${menu[option]["cost"]:.2f}", end="    ")
    print()


def show_report(resource_data, money_amount):
    """Print the current quantity of each resource and the amount of money.

    Args:
        resource_data (dict): The dictionary that contains the resources (as keys), their quantities and their unit of measurement (as a list). 
        money_amount (int): The amount of money that has been collected.
    """
    for resource, quantity in resource_data.items():
        print(f"{resource.title()}: {quantity[0]}{quantity[1]}")
    print(f"Money: ${money_amount:.2f}")


def is_resources_sufficient(order_ingredients, resource_data):
    """Return True if the order can be made, False if the resources are insufficient.

    Args:
        order_ingredients (dict): The dictionary that contains the ingredients needed to make the order.
        resource_data (dict): The dictionary that contains the resources (as keys), their quantities and their unit of measurement (as a list).

    Returns:
        bool
    """
    for resource, quantity in order_ingredients.items():
        if resource_data[resource][0] < quantity:
            print(f"Sorry, there is not enough {resource}.")
            return False
        return True


def process_payment():
    """Returns the total calculated from coins inserted.

    Returns:
        float
    """
    print("Please insert coins.")
    total = int(input("how many fifty cent coins?: ")) * 0.50
    total += int(input("how many twenty-five cent coins?: ")) * 0.25
    total += int(input("how many ten cent coins?: ")) * 0.1
    total += int(input("how many five cent coins?: ")) * 0.05
    total += int(input("how many one cent coins?: ")) * 0.01
    return total
    #A digit verification to prevent errors would be nice


def is_transaction_successful(money_received, order_cost):
    """Return True when the payment is accepted, or False if money is insufficient. increases the money collected by the machine and calculates the change that the user needs to receive back.

    Args:
        money_received (float): Total value from the coins inserted
        order_cost (float): Total cost of the order.

    Returns:
        bool
    """
    if money_received >= order_cost:
        change = money_received - order_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        global money
        money += order_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order, resources_data, order_ingredients):
    """Deduct the required ingredients from the resources and print a message according to the order.

    Args:
        order (str): The order from the user.
        resources_data (dict): The dictionary that contains the resources (as keys), their quantities and their unit of measurement (as a list).
        order_ingredients (dict): The dictionary that contains the ingredients needed to make the order.
    """
    for ingredient, quantity in order_ingredients.items():
        resources_data[ingredient][0] -= quantity
    print(f"Here is your {order.title()} ☕. Enjoy!")


def refill(resources_data):
    """Allows resource quantities to be increased through inputs.

    Args:
        resources_data (dict): The dictionary that contains the resources (as keys), their quantities and their unit of measurement (as a list).
    """
    for resource in resources_data:
        quantity = int(input(f"How much {resource} will be refiled (in {resources_data[resource][1]}): "))
        resources_data[resource][0] += quantity


def coffe_machine():
    show_options(MENU)
    while True:
        user_choice = input(f"What would you like: ").lower()
        if user_choice == "report":
            show_report(resources, money)
        elif user_choice == "off":
            return
        elif user_choice == "refill":
            refill(resources)
        elif user_choice in MENU.keys():
            if is_resources_sufficient(MENU[user_choice]["ingredients"], resources):
                received_coins = process_payment()
                if is_transaction_successful(received_coins, MENU[user_choice]["cost"]):
                    make_coffee(user_choice, resources, MENU[user_choice]["ingredients"])


coffe_machine()
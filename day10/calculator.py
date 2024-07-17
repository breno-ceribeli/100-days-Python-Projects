from art import logo
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def roundFloat(num):
    # Converts the number to string
    strNum = str(num)

    # Removes leading and trailing zeros
    strNum = strNum.rstrip('0').rstrip('.')

    # If after removing all leading and trailing zeros and the decimal point, the string becomes empty, return 0
    if strNum == '':
        return 0
    
    # Converts back to float
    return float(strNum) if '.' in strNum else int(strNum)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# recursion
def calculator():
    print(logo)
    num1 = float(input("First number: "))

    print("Pick a operation by its symbol.")
    operationList = ""
    # Iterates over the dictionary items, unpacking each key-value pair into 'symbol' and 'function'.
    # Prints the operation symbol and the name of the corresponding function.
    for symbol, function in operations.items():
        operationList += f"{function.__name__.title()}: {symbol} | "
    # Prints all elements of 'operationList' except the last three. Slicing
    print(operationList[:-3])
    # or print(operationList.rstrip(" | "))

    shouldContinue = True
    while shouldContinue:
        operationSymbol = input("Operation: ")

        num2 = float(input("Next number: "))
        while num2 == 0 and operationSymbol == "/":
            num2 = float(input("It's not possible to divide by 0, please type another number: "))

        calculationFunction = operations[operationSymbol]
        result = calculationFunction(num1, num2)

        print(f"{roundFloat(num1)} {operationSymbol} {roundFloat(num2)} = {roundFloat(result)}")

        restart = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()
        if restart == 'y':
            num1 = result
        elif restart == 'n':
            shouldContinue = False
            clear_console()
            calculator()
        else:
            shouldContinue = False

calculator()
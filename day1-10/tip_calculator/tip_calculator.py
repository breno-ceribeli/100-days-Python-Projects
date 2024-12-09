print("Welcome to the Tip Calculator")
#Receives the data that is needed to calculate
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))
#Doing the calculation
tipAsPercent = tip / 100 + 1
totalBill = bill * tipAsPercent
billPerPerson = totalBill / people
#Showing the results and assuring that it's shown with two digits
finalAmount = '{0:.2f}'.format(billPerPerson)
#OR finalAmount = "%.2f" % billPerPerson
print(f"Each person should pay: ${finalAmount}")
#OR print(f"Each person should pay: ${billPerPerson:.2f}")
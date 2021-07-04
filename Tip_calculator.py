# This is a tip calculator, to calculate the bill you will pay after adding the % of tip you want to give.
# This can also be used to split the bill among a group of people dining together.
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 0, 5, 10, 12, or 15? "))
no_of_person = int(input("How many people to split the bill? "))
total_bill =  bill + (bill * (tip/100))
bill_split = round(total_bill / no_of_person, 2)
print(f"Each person should pay: ${bill_split}")
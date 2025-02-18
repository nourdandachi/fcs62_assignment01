print("Hello Nabiha!")
salary = int(input("Please enter your salary: "))

month = input("Please enter the month you want to store the salary for: ")

while month != "January" and month != "February" and month != "March" and month != "April" and month != "May" and month != "June" and month != "July" and month != "August" and month != "September" and month != "October" and month != "November" and month != "December":
    month = input("Please enter a valid month: ")

print ("Please enter the following percentages respectively:")

savings_percentage = int(input("Saving: "))
while savings_percentage>100 or savings_percentage<0:
    savings_percentage = int(input("Enter a valid number. Saving: "))

rent_percentage = int(input("Rent: "))
while rent_percentage>100 or rent_percentage<0:
    rent_percentage = int(input("Enter a valid number. Rent: "))

electricity_percentage = int(input("Electricity: "))
while electricity_percentage>100 or electricity_percentage<0:
    electricity_percentage = int(input("Enter a valid number. Electricity: "))
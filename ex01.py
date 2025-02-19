print("Hello Nabiha!")
salary = int(input("Please enter your salary: "))

month = input("Please enter the month you want to store the salary for: ")

while month != "January" and month != "February" and month != "March" and month != "April" and month != "May" and month != "June" and month != "July" and month != "August" and month != "September" and month != "October" and month != "November" and month != "December":
    month = input("Please enter a valid month: ")

print ("Please enter the following percentages respectively:")

savings_percentage = int(input("Savings: "))
while savings_percentage>100 or savings_percentage<0:
    savings_percentage = int(input("Enter a valid number. Savings %: "))

rent_percentage = int(input("Rent: "))
while rent_percentage>100 or rent_percentage<0:
    rent_percentage = int(input("Enter a valid number. Rent %: "))

electricity_percentage = int(input("Electricity: "))
while electricity_percentage>100 or electricity_percentage<0:
    electricity_percentage = int(input("Enter a valid number. Electricity %: "))

saving_amount= (salary * savings_percentage)/100
rent_amount= (salary * rent_percentage)/100
electricity_amount= (salary * electricity_percentage)/100

total_spent_amount= saving_amount + rent_amount + electricity_amount

remainder_amount= salary - total_spent_amount

yearly_rent = rent_amount * 12 
yearly_electricity_cost= electricity_amount * 12

my_dream_salary= salary * salary  #or we can use the pow() function: squared_salary= pow(salary,2)

print("Did you save any additional amount this month?")
answer= input("(Y or N): ")
if answer == "Y":
    additional_amount= int(input("Enter the amount: "))
    while additional_amount<0:
        additional_amount = int(input("Enter a valid number: "))
    
    additional_savings = additional_amount/saving_amount

print("Lets summarize your month based on your inputs:")
print("For this month:" )
print("--> Your saving amount is:", saving_amount, "$ as", savings_percentage, "% of your salary.")
print("--> Your rent amount:", rent_amount,"$ as", rent_percentage, "% of your salary.")
print("--> Your electricity amount:", electricity_amount,"$ as", electricity_percentage, "% of your salary.")
print(" ")
print("So your total spent amount for this month is",total_spent_amount,"$, with a remainder of",remainder_amount,"$ from your initial salary.")
print("--> Your yearly amount of rent and electricity bills are:",yearly_rent,"and",yearly_electricity_cost,"respectively")
if answer == "Y":
    print("--> Your additional savings for this month are equivalent to",additional_savings,"of your initial savings amount")
print("--------------------")
print("--> Nabiha's dream monthly salary, mine also :) , is:", my_dream_salary,"$.")


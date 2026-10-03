Employee_name = input("Enter employee name: ")
Basic_Salary = int(input("Enter basic salary: "))
Years_of_service = int(input("Enter years of service: "))

print("Employee Name: ", Employee_name)
print("Basic Salary: ", Basic_Salary)
print("Years of Service: ", Years_of_service)


HRA = 0.20 * Basic_Salary
print("HRA: ", HRA)

DA = 0.10 * Basic_Salary
print("DA:", DA)

Gross_Salary = Basic_Salary + HRA + DA
print("Gross Salary: ", Gross_Salary)

TAX = 0.05 * Gross_Salary
print("TAX: ", TAX)

if Years_of_service > 5:
    Bonus_percentage = "10%"
    Bonus_amount = 0.10 * Basic_Salary
    print("Bonus_percentage: ", Bonus_percentage)
    print("Bonus_amount: ", Bonus_amount)

elif Years_of_service >= 3:
    Bonus_percentage = "5%"
    Bonus_amount = 0.05 * Basic_Salary
    print("Bonus_percentage: ", Bonus_percentage)
    print("Bonus_amount: ", Bonus_amount)

else:
    Bonus_percentage = "0%"
    Bonus_amount = 0
    print("Bonus_percentage: ", Bonus_percentage)
    print("Bonus_amount: ", Bonus_amount)

Net_Salary = Gross_Salary - TAX + Bonus_amount
print("Net Salary: ", Net_Salary)
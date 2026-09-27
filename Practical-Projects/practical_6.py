basic_salary = int(input("Enter basic salary: "))
print("Basic salary:", basic_salary)

HRA = 0.2 * basic_salary
print("HRA:", HRA)

DA = 0.1 * basic_salary
print("DA:", DA)

Gross_salary = basic_salary + HRA + DA
print("Gross salary:", Gross_salary)

Tax =  Gross_salary * 5 / 100
print("Tax:", Tax)

Net_salary = Gross_salary - Tax
print("Net salary:", Net_salary)
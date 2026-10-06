Employee_name = "Aliya"
Basic_salary = 40000
Working_days = 48
print("Employee Name:", Employee_name)
print("Basic Salary:", Basic_salary)
print("Working Days:", Working_days)

overtime_hours = 8
print("Overtime Hours:", overtime_hours)

overtime_rate = 250
overtime_pay = overtime_hours * overtime_rate
print("Overtime Rate:", overtime_rate)
print("Overtime Pay:", overtime_pay)

Gross_salary = Basic_salary + overtime_pay
print("Gross Salary:", Gross_salary)

TAX = Gross_salary * 5 / 100
print("TAX:", TAX)

Net_salary = Gross_salary - TAX
print("Net Salary:", Net_salary)
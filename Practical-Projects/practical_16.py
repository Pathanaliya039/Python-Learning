Employee_name = "Aliya"
Basic_salary = 40000
Working_days = 26
level_days = 2
print("Employee Name:", Employee_name)
print("Basic Salary:", Basic_salary)
print("Working Days:", Working_days)
print("Level Days:", level_days)


Daliy_salary = round(Basic_salary / Working_days, 2) 
print("Daily Salary:", Daliy_salary)

Level_deduction = round(Daliy_salary * level_days, 2)
print("Level Deduction:", Level_deduction)

Salary_after_deduction = round(Basic_salary - Level_deduction, 2)
print("Salary after Deduction:", Salary_after_deduction)


if level_days >= 2:
    level_status = "Level Approved"
    print("Level Status:", level_status)
elif level_days >= 5:
    Level_status = "Level Warning"
    print("Level Status:", Level_status)
else:
    Level_status = "Level Not Approved"
    print("Level Status:", Level_status)


if level_status == "Level Approved":
    Salary_status = "Salary Processed"
    print("Salary Status:", Salary_status)
elif level_status == "Level Warning":
    Salary_status = "Salary Processed with Warning"
    print("Salary Status:", Salary_status)
else:
    Salary_status = "Salary on Hold"
    print("Salary Status:", Salary_status)
employee_name = "Aliya"
sales_amount = 85
performance_rating = 4

print("Employee Name:", employee_name)
print("Sales Amount:", sales_amount)
print("Performance Rating:", performance_rating)

performance_score = sales_amount * performance_rating

print("Performance Score:", performance_score)

if performance_score >= 300:
    performance_level = "Excellent"
elif performance_score >= 200:
    performance_level = "Good"
elif performance_score >= 100:
    performance_level = "Average"
else:
    performance_level = "Needs Improvement"

print("Performance Level:", performance_level)

salary = 30000

if performance_level == "Excellent":
    bonus_percentage = 10
elif performance_level == "Good":
    bonus_percentage = 7
elif performance_level == "Average":
    bonus_percentage = 5
else:
    bonus_percentage = 0

bonus_amount = salary * bonus_percentage / 100

print("Salary:", salary)
print("Bonus Percentage:", bonus_percentage, "%")
print("Bonus Amount:", bonus_amount)

    


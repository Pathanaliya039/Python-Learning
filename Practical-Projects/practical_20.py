employee_name = "Aliya"
monday_task = 8
tuesday_task = 10
wednesday_task = 7
weekly_task = 40
print("Employee Name:", employee_name)
print("Monday Task:", monday_task)
print("Tuesday Task:", tuesday_task)
print("Wednesday Task:", wednesday_task)
print("Weekly Task:", weekly_task)

total_tasks = monday_task + tuesday_task + wednesday_task
print("Total Task:", total_tasks)

number_of_days = 3
average_tasks = round((total_tasks / number_of_days),2)
print("Number of days :", number_of_days)
print("Average Task:", average_tasks)

remaining_tasks = weekly_task - total_tasks
print("Remaining Tasks:", remaining_tasks)


if total_tasks >= weekly_task:
    print("Target Achieved")
else:
    print("Target Not Achieved")


Target_Percentage = round((total_tasks / weekly_task) * 100 ,2)
print("Target Percentage:", Target_Percentage)

if Target_Percentage >= 100:
    productivity_level = "High Productivity"
    print("Productivity Level:", productivity_level)
elif Target_Percentage >= 75:
    productivity_level = "Good Productivity"
    print("Productivity Level:", productivity_level)
else:
    productivity_level = "Needs Improvement"
    print("Productivity Level:", productivity_level)
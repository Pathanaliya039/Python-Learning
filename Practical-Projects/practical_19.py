student_name = "Aliya"
monday_hours = 2
tuesday_hours = 3
wednesday_hours = 1
weekly_study_goal = 15
print("Student Nmae:", student_name)
print("Monday Hours:", monday_hours)
print("Tuesday Hours:", tuesday_hours)
print("Wednesday Hours:", wednesday_hours)
print("Weekly Study Goal:", weekly_study_goal)

Total_study_hours = monday_hours + tuesday_hours + wednesday_hours
print("Total Study Hours:", Total_study_hours)

Number_of_days = 3
average_study_hours = round( Total_study_hours / Number_of_days)
print("number of days:", Number_of_days)
print("Average Study Hours:", average_study_hours)

remaining_study_hours = weekly_study_goal - Total_study_hours
print("Remaining Study Hours:", remaining_study_hours)


if Total_study_hours >= weekly_study_goal:
    print("Weekly Goal Achieved")
else:
    print("Weekly Goal Not Achieved")


Study_Percentage = round((Total_study_hours / weekly_study_goal) * 100, 2)
print("Study Percentage:", Study_Percentage)


if Study_Percentage >= 100:
    print("Goal Completed")
elif Study_Percentage >= 50:
    print("Good Progress")
else:
    print("Needs More Study")


person_name = "Aliya"
saving_goal = 50000
current_savings = 18000
monthly_savings = 5000
print("Person Name:", person_name)
print("Saving Goal:", saving_goal)
print("Current Saving:", current_savings)
print("Monthly Saving:", monthly_savings)

Total_savings = current_savings + monthly_savings
print("Total Savings :", Total_savings)


Remaining_savings = saving_goal - Total_savings
print("Remaining_savings:", Remaining_savings)

if Total_savings >= saving_goal:
    goal_status = "Goal Achieved"
else:
    goal_status = "Goal Not Achieved"
print("goal_status:", goal_status)

Goal_Percentage = round((Total_savings / saving_goal) * 100)
print("Goal Percentage:", Goal_Percentage, "%")

if Goal_Percentage >= 100:
    progress_status = "Goal Completed"
elif Goal_Percentage >= 50:
    progress_status = "Good Progress"
else:
    progress_status = "Needs More Savings"
print("Progress Status:", progress_status)

person_name = "Aliya"
monthly_budget = 15000
food_expenses = 3500
travel_expenses = 2000
shopping_expenses = 2500

print("Person_Name:", person_name)
print("Monthly_Budget:", monthly_budget)
print("Food_Expenses:", food_expenses)
print("Travel_Expenses:", travel_expenses)
print("Shopping_Expenses:", shopping_expenses)

total_expenses = food_expenses + travel_expenses + shopping_expenses
print("Total_Expenses:", total_expenses)

Remaining_budget = monthly_budget - total_expenses
print("Remaining_Budget:", Remaining_budget)

if total_expenses <= monthly_budget:
    budget_status = "Within Budget"
    print("Budget Status:", budget_status)
else:
    budget_status = "Over Budget"
    print("Budget Status:", budget_status)

Budget_Usage_Percentage = round((total_expenses / monthly_budget) * 100, 2)
print("Budget Usage Percentage:", Budget_Usage_Percentage, "%")


if Budget_Usage_Percentage >= 80:
    spending_status = "High Spending"
    print("Spending Status:", spending_status)
elif Budget_Usage_Percentage >= 50:
    spending_status = "Moderate Spending"
    print("Spending Status:", spending_status)
else:
    spending_status = "Low Spending"
    print("Spending Status:", spending_status)



print(f"""
=====================PERSONAL EXPENSE BUDGET ANALYZER=====================
Person Name: {person_name}
Monthly Budget: {monthly_budget}
Food Expenses: {food_expenses}
Travel Expenses: {travel_expenses}
Shopping Expenses: {shopping_expenses}
Total Expenses: {total_expenses}
Remaining Budget: {Remaining_budget}
Budget Status: {budget_status}
Budget Usage Percentage: {Budget_Usage_Percentage}%
Spending Status: {spending_status}
===================================================================================""")

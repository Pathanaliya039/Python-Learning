expenses = [250, 120, 500, 80, 300]
print("Expenses:", expenses)

sum_expenses = sum(expenses)
print("Total Expenses:", sum_expenses)

max_expenses = max(expenses)
print("Maximum Expenses:", max_expenses)

min_expenses = min(expenses)
print("Minimum Expenses:", min_expenses)

len_expenses = len(expenses)
print("Number of Expenses:", len_expenses)

average_expenses = sum_expenses / len_expenses
print("Average Expenses:", average_expenses)

expenses.append(200)
print("Updated Expenses:", expenses)

for expense in expenses:
    print("Expenses:", expense)
Employee_name = "Aliya"
total_days = 26
present_days = 23
performance_days = 4

print("Employee Name:", Employee_name)
print("Total Days:", total_days)
print("Present Days:", present_days)
print("Performance Days:", performance_days)

Attendance_percentage = round((present_days / total_days) * 100, 2)
print("Attendance Percentage:", Attendance_percentage, )

if Attendance_percentage >= 90:
    Attendance_Status = "Excellent Attendance"
    print("Attendance Status:", Attendance_Status)
elif Attendance_percentage >= 80:
    Attendance_Status = "Good Attendance"
    print("Attendance Status:", Attendance_Status)
elif Attendance_percentage >= 70:
    Attendance_Status = "Poor Attendance"
    print("Attendance Status:", Attendance_Status)

if performance_days >= 5:
    performance_level = "Excellent Performance"
    print("Performance Level:", performance_level)
elif performance_days >= 4:
    performance_level = "Good Performance"
    print("Performance Level:", performance_level)
elif performance_days >= 3:
    performance_level = "Average Performance"
    print("Performance Level:", performance_level)
else:
    performance_level = "Poor Performance"
    print("Performance Level:", performance_level)

if Attendance_percentage >= 90 and performance_days == 5:
    incentive_status = "Eligible for 10% Incentive"
elif Attendance_percentage >= 75 and performance_days >= 4:
    incentive_status = "Eligible for 5% Incentive"
else:
    incentive_status = "Not Eligible for Incentive"

print("Incentive Status:", incentive_status)

Basic_salary = 40000
print("Basic Salary:", Basic_salary)
incentive_status = "5%"

if incentive_status ==  "10%":
    incentive_amount = Basic_salary * 0.10
    print("Incentive Amount:", incentive_amount)
elif incentive_status == "5%":
    incentive_amount = Basic_salary * 0.05
    print("Incentive Amount:", incentive_amount)
else:
    incentive_amount = 0
    print("Incentive Amount:", incentive_amount)
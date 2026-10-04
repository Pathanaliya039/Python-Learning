student_name = input("Enter your name: ")
percentage = int(input("Enter your percentage: "))
family_income = int(input("Enter your family income: "))

print("Student Name:", student_name)
print("Percentage:", percentage)
print("Family Income:", family_income)


if percentage >= 90:
    Grade = "A+"
    print("Grade:", Grade)
elif percentage >= 80:
    Grade = "A"
    print("Grade:", Grade)
elif percentage >= 70:
    Grade = "B"
    print("Grade:", Grade)
elif percentage >= 60:
    Grade = "C"
    print("Grade:", Grade)
else:
    Grade = "D"
    print("Grade:", Grade)


if percentage >= 80 and family_income < 250000:
        scholarship_status = "Eligible for scholarship"
        print("Scholarship:", scholarship_status)
else:
    scholarship_status = "Not eligible for scholarship"
    print("Scholarship:", scholarship_status)


if Grade == "A+":
    Scholarship_amount = 20000
    print("Scholarship Amount:", Scholarship_amount)
elif Grade == "A":
    Scholarship_amount = 15000
    print("Scholarship Amount:", Scholarship_amount)
elif Grade == "B":
    Scholarship_amount = 10000
    print("Scholarship Amount:", Scholarship_amount)
elif Grade == "C":
    Scholarship_amount = 5000
    print("Scholarship Amount:", Scholarship_amount)
else:
    Scholarship_amount = 0
    print("Scholarship Amount:", Scholarship_amount)

if scholarship_status == "Eligible for Scholarship":
    final_Decision = "Scholarship Approved"
    print("Final Decision:", final_Decision)
else:
    final_Decision = "Scholarship Not Approved"
    print("Final Decision:", final_Decision)
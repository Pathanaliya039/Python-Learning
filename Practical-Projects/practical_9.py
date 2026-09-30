student_name = input("Enter student name")
course_fee = int(input("Enter course fee"))
amount_paid = int(input("Enter paid amount"))

print("Student_Name:", student_name)
print("Course_Fee:", course_fee)
print("Amount_Paid:", amount_paid)
 
Remaining_Fee = course_fee - amount_paid
print("Remaining_Fee:", Remaining_Fee)

Paid_Percentage = amount_paid / course_fee * 100
print("Paid_Percentage:", Paid_Percentage)

if Remaining_Fee <= 0:
    Fee_Status = "Fully Paid"
elif Remaining_Fee <= 10000:
    Fee_Status = "Almost Paid"
else:
    Fee_Status = "Payment Pending"

print("Fee_Status:", Fee_Status)

if Fee_Status == "Fully Paid":
    late_Charge = 0
elif Fee_Status == "Almost Paid":
    late_Charge = 500
else:
    late_Charge = 1000

print("Late_Charge:", late_Charge)

Total_Due = Remaining_Fee + late_Charge
print("Total_Due:", Total_Due)


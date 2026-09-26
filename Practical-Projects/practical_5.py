total_classes = int(input("Enter total classes : "))
classes_attended = int(input("Enter classes attended: "))
print("Total classes :", total_classes)
print("Classes attended :", classes_attended)

Attended_percentage = (classes_attended / total_classes) * 100
print("Attended percentage :", Attended_percentage)

if Attended_percentage >= 75:
    print("Eligible.")
else:
    print("Not eligible.")


if Attended_percentage >= 85:
    print("Eligible")
elif Attended_percentage >= 70:
    print("Warning: Attendance is low")
else:
    print("Not eligible")

if total_classes < 0:
    print("Invalid attendance data.")
elif classes_attended < 0:
    print("Invalid attendance data.")
else:
    print("Attendance data is valid.")

if Attended_percentage >= 85:
    print("You are eligible for the exam.")
elif Warning:
    print(" Please improve your attendance.")
else:
    print("You are  currently not eligible for the exam.")
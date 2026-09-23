marks = int(input("Enter your marks: "))

if marks >= 40:
    print("passed")
else:
    print("failed")

if marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")

if marks < 0 or marks > 100:
    print("Invalid marks ")

if marks >= 40:
    passed = True
    print("Congratulations! You passed")

else:
    print("Better luck next time!")

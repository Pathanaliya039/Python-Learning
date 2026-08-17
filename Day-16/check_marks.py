def check_marks(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"


result = check_marks(82)

print("Result:", result)
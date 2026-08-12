student = {
    "name": "Aliya",
    "age": 20,
    "course": "BCS",
    "city": "Daund"
}

print("Course:",
student.get("course"))

student.pop("city")

print("After removing city:", student)
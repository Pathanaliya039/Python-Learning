student = {
    "name": "Aliya",
    "age": 19,
    "course": "BCS",
    "city":"Daund"
}

for key, value in student.items():
    if key == "name" or key == "course":
        print(value)
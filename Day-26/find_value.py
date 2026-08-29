def find_value(data, key):
    return data[key]


student = {
    "name": "Aliya",
    "age": 19,
    "course": "BCS"
}

result = find_value(student, "course")

print("Course:", result)
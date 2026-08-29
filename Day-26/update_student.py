def update_age(student, new_age):
    student["age"] = new_age
    return student


student = {
    "name": "Aliya",
    "age": 19,
    "course": "BCS"
}

result = update_age(student, 20)

print("Update student:", result)



    
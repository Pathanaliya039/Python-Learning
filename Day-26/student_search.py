def search_student(students, name):
    if name in students:
        student = students[name]
        return student
    return "Student not found"


student = {
    "Aliya": {"age": 19, "course": "BCS"},
    "Sara": {"age": 20, "course": "BCA"},
    "Ayesha":{"age": 19, "course": "BSC"}
}

result = search_student(student, "Aliya")

print("Student details:", result)
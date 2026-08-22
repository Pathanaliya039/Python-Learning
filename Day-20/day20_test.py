#Task 1
def add_subject(subjects, new_subject):
    subjects.append(new_subject)
    return subjects


subjects = ["Python", "DBMS", "DSA"]

result = add_subject(subjects, "C")

print("Updated list:", result)


#Task 2
def remove_subject(subjects, subject):
    subjects.remove(subject)
    return subjects


subjects = ["Python", "DBMS", "DSA", "C"]

result = remove_subject(subjects, "DBMS")

print("Updated list:", result)


#Task 3
def update_subject(subjects, index, new_subject):
    subjects[index] = new_subject
    return subjects


subjects = ["Python", "DBMS", "DSA"]

result = update_subject(subjects, 1, "MySQL")

print("Updated list:", result)
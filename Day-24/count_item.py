def count_item(items, target):
    count = 0

    for item in items:
        if item == target:
            count = count + 1

    return count


items = ["Python", "C", "Python", "DBMS", "Python"]

result = count_item(items, "Python")

print("Count:", result)
def find_item(items, target):
    for item in items:
        if item == target:
            return item

    return None


items = ["Python", "C", "Java", "DBMS"]

result = find_item(items, "Python")

print("Found:", result)
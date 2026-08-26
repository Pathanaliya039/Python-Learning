def remove_item(items, target):
    result = []

    for item in items:
        if item != target:
            result.append(item)

    return result


items = ["Python", "C", "Python", "DBMS"]

result = remove_item(items, "Python")

print("Updated list:", result)
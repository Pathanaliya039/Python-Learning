def find_position(items, target):
    for index in range(len(items)):
        if items[index] == target:
            return index

    return -1

items = ["Python", "C", "Java", "SQL"]

result = find_position(items, "Java")

print("Position:", result)
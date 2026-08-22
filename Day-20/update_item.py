def update_item(items, index, new_item):
    items[index] = new_item
    return items


items = ["Python", "C", "Java", "SQL"]

result = update_item(items, 1, "C++")

print("Update list:", result)
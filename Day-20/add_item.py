def add_item(items, new_item):
    items.append(new_item)
    return items


items = ["Python", "C", "Java"]

result = add_item(items, "SQL")

print("Updated list:", result)
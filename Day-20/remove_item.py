def remove_item(items, item):
    items.remove(item)
    return items


items = ["Python", "C", "Java","SQL"]

result = remove_item(items, "C")

print("Updated list:",result)
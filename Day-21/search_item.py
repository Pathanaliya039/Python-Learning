def search_item(items, target):
    for item in items:
        if item == target:
            return "Found"

    return "Not Found"


items = ["Python", "C", "Java", "SQL"]

result = search_item(items, "Java")

print("Result:", result)
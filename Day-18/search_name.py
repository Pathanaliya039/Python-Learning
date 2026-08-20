def search_name(name,target):
    for name in names:
        if name == target:
            return "Found"

    return "Name"

names = ["Aliya, Sara", "Ayesha", "Zoya"]

result = search_name(names, "Ayesha")

print("Name:", result)

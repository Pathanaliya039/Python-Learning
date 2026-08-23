def reverse_list(items):
    reversed_list = []

    for index in range(len(items)-1, -1, -1):
        reversed_list.append(items[index])

    return reversed_list

items =[10, 20, 30, 40, 50]

result = reverse_list(items)

print("Reversed:", result)
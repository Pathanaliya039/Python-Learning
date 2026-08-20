def search_number(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False

number = [10,20,30,40,50]

result = search_number(number, 30)

print("Found:", result)
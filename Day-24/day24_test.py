def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [25, 10, 45, 5, 30]

result = find_largest(numbers)

print("Largest:", result)
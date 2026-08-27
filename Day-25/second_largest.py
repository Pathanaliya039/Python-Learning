def find_second_largest(numbers):
    numbers.sort()
    return numbers


numbers = [25, 10, 45, 5, 30]

result = find_second_largest(numbers)

print("Second Largest:", result)
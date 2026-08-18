def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:

        if number > largest:

            largest = number

    return largest

numbers = [10,45,23,67,12]

answer = find_largest(numbers)

print("Largest:", answer)
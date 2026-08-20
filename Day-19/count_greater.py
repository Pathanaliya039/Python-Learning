def count_greater(numbers, target):
    count = 0

    for number in numbers:
        if number > target:
            count = count + 1

    return count

numbers = [10, 25, 5, 40, 15, 30]

result = count_greater(numbers, 20)

print("Count:", result)
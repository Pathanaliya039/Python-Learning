def sum_even(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total = total + number

    return total

numbers = [5, 10, 15, 20, 25, 30]

result = sum_even(numbers)

print("Sum of even numbers:", result)
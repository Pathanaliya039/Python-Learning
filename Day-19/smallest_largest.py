def find_min_max(numbers):
     smallest = numbers[0]
     largest = numbers[0]

     for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

     return smallest, largest

numbers = [25, 10, 45, 5, 30]

small, large = find_min_max(numbers)

print("Smallest:", small)
print("Largest:", large)
#Task 1
def sum_odd(numbers):
    total = 0

    for number in numbers:
        if number % 2 != 0: 
           total = total + number

    return total

numbers = [5, 10, 15, 20, 25,30]

result = sum_odd(numbers)

print("Sum of odd numbers:", result)


#Task 2
def count_less(numbers, target):
    count = 0

    for number in numbers:
        if number < target:
            count = count + 1

    return count

numbers = [10, 25, 5, 40, 15, 30]

result = count_less(numbers, 20)

print("Count:", result)


#Task 3
def find_min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    
    for number in numbers:
            if number < smallest:
                smallest = number
    
            if number > largest:
                largest = number
    
    return smallest, largest
    
numbers = [18, 7, 32, 4, 25]
    
small, large = find_min_max(numbers)
    
print("Smallest:", small)
print("Largest:", large)

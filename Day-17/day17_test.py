#Task 1
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total
        
numbers = [5,10,15,20]

answer = calculate_sum(numbers)
        
print("Sum:", answer)


#Task 2
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1

numbers =[2,5,8,11,14,17]

answer = count_even(numbers)

print("Even:", answer)

#Task 3
def find_smallest(numbers):
    smallest = numbers[0]
    
    for number in numbers:
    
            if number < smallest:
    
                smallest = number
    
    return smallest
    
numbers = [25,10,45,5,30]
    
answer = find_smallest(numbers)
    
print("Smallest:", answer)
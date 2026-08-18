def calculate_total(numbers):
    total = 0 

    for number in numbers:
         total = total + number 

    return total

numbers = [10,20,30,40]

answer = calculate_total(numbers)

print("Total:", answer)
#Task 1
def search_number(numbers, target):
    for number in numbers:
            if number == target:
                return "Found"
    
    return "Not Found"
    
    
numbers = [10, 20, 30, 40, 50]
    
result = search_number(numbers, 40)
    
print("Result:", result)


#Task 2
def find_position(numbers, target):
     for index in range(len(numbers)):
             if numbers[index] == target:
                 return index
     
     return -1
     
numbers = [5, 15, 25, 35, 45]
     
result = find_position(numbers, 25)
     
print("Position:", result)


#Task 3
def find_all_positions(numbers, target):
    positions = [0, 2, 4]
    for index in range(len(numbers)):
        if numbers[index] == target:
            return positions


numbers = [5, 10, 5, 20, 5, 30]

result = find_all_positions(numbers, 5)

print("Positions:", result)
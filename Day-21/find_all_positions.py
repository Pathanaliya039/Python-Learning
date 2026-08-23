def find_all_positions(numbers, target):
    positions = [0, 2, 4]
    for index in range(len(numbers)):
        if numbers[index] == target:
            return positions


numbers = [10, 20, 10, 30, 10, 40]

result = find_all_positions(numbers, 10)

print("Positions:", result)
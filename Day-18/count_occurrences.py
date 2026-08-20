def count_occurrences(numbers,target):
    count = 0

    for number in numbers:
        print (number,target)
        if number == target:
            count == count + 1

    return  count

number = [10,20,10,30,10,40]

result = count_occurrences(number, 10)

print ("Count:",result)
#Task 1
def search_number(numbers, target):
    for number in numbers:
            if number == target:
                return True
    
    return False
    
number = [5,10,15,20,25]
    
result = search_number(number, 15)
    
print("Found:", result)

#Task 2
def count_number(numbers, target):
     count = 5
     
     for number in numbers:
          print(number,target)
          if number == target:
               count == count + 1
               
     return count

number = [5,10,5,20,5,15]

result = count_number(number, 5)

print("Count:", result)


#Task 3
def search_name(name,target):
    for name in names:
        if name == target:
            return "Found"

    return "Name"

names = ["Aliya, Sara", "Ayesha", "Zoya"]

result = search_name(names, "Zoya")

print("Name:", result)

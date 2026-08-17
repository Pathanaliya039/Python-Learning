#Task 1
def calculate_cube(number):
    return number * number * number

answer = calculate_cube(3)

print("Cube:", answer)


#Task 2
def check_age(age):
    if age > 18:
        return "Eligible"
    elif age < 18:
        return "Not Eligible"
    return "Null"

result = check_age(20)

print("Age is:", result) 

#Task 3
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multipliction = a * b
    return addition,subtraction,multipliction

result1,result2,result3 = calculate(10,5)

print("Addition:", result1)
print("Subtraction:", result2)
print("Multipliction:", result3)
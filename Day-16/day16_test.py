#Task 1
def subtract(b , a):
    result = b - a
    return result

answer = subtract(20 , 8)

print("Answer:", answer)

#Task 2
def check_temperature(temp):
    if temp >= 30:
       return "Hot"
    elif temp >= 20: 
       return "Normal"
    else:
       return "Cold"

result = check_temperature(25)

print("Result:", result)


#Task 3
def check_number(number):
   if number > 0:
      return "Positive"
   elif number < 0:
      return "Negative"
   else: 
      return "Zero"

   print(check_number(10))
   print(check_number(-5))
   print(check_number(0)) 
   
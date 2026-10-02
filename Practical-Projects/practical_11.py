# ELECTRICITY BILL 

consumer_name = input("Enter consumer name: ")
Units = int(input("Enter number of units consumed: "))
print("Consumer Name:", consumer_name)
print("Units Consumed:", Units)

if Units <= 100:
    rate_per_unit = 5
    print("Rate per unit:", rate_per_unit)
    
elif Units <= 200:
    rate_per_unit = 7
    print("Rate per unit:", rate_per_unit)
    
else:
    rate_per_unit = 10
    print("Rate per unit:", rate_per_unit)


Energy_Charge = Units * rate_per_unit
print("Energy_Charge:", Energy_Charge)


if Units <= 100:
    Fixed_Charge = 50 
    print("Fixed_Charge:", Fixed_Charge)
elif Units <= 200:
    Fixed_Charge = 100
    print("Fixed_Charge:", Fixed_Charge)
else:
    Fixed_Charge = 150
    print("Fixed_Charge:", Fixed_Charge)

Subtotal = Energy_Charge + Fixed_Charge
print("Subtotal:", Subtotal)


GST = Subtotal * 5 / 100
print("GST:", GST)

Final_Bill = Subtotal + GST
print("Final_Bill:",Final_Bill)

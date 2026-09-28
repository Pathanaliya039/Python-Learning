item_price = int(input("Enter item price"))
quantity = int(input("Enter quantity"))

print("item_price:", item_price)
print("quantity:", quantity)

subtotal = item_price * quantity
print("subtotal:", subtotal)

GST = subtotal * 18/100
print("GST:", GST)

Final_Bill = subtotal + GST
print("Final_Bill:", Final_Bill)

if subtotal >= 1000:
    discount = Final_Bill * 10/100
    print("discount:", discount)
else:
    discount = 0
    print("discount:", discount)

Final_Amount = subtotal - discount + GST
print("Final Amount:", Final_Amount)
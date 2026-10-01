# INVENTORY SUMMARY

product_name = input("Enter the product name: ")
price = int(input("Enter the price of one item: "))
quantity = int(input("Enter the number of items in stock: "))

print("product name:", product_name)
print("price:", price)
print("quantity:", quantity)

Total_value = price * quantity
print("Total value of the stock:", Total_value)

if quantity == 0:
    print("The product is out of stock.")
elif quantity <= 9:
    print("The product is low stock.")
else:
    print("The product in stock.")

if quantity  <= 5:
    print("Reorder Required.")
else:
    print("Stock Level ok.")

if quantity > 20:
    discount_percentage = 5
    print("discount percentage: 5%")
else:
    discount_percentage = 0
    print("discount percentage: 0%")

Discount_amount = Total_value * discount_percentage / 100
print("Discount amount:", Discount_amount)

Final_Stock_value = Total_value - Discount_amount
print("Final Stock value:", Final_Stock_value)
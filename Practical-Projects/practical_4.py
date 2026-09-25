prices = [100, 250, 75, 300, 150]
print("prices:", prices)

total_prices = sum(prices)
print("Total prices:", total_prices)

highest_price = max(prices)
print("Highest price:", highest_price)

lowest_price = min(prices)
print("Lowest price:", lowest_price)

if total_prices  >= 800:
    calculate_discount = total_prices * 10 /100
    print("Discount calculated:", calculate_discount)

final_price = total_prices - calculate_discount
print("Final price after discount:", final_price)

print("total_prices:", total_prices)
print("discount:", calculate_discount)
print("final_price:", final_price)
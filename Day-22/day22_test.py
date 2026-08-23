def check_palindrome(items):
    reversed_items = items[::-1]
    
    if items == reversed_items:
        return "palindrome"
    else:
        return "Not Palindrome"
    
    
numbers1 = [1, 2, 3, 2, 1]
numbers2 = [10, 20, 30, 40]
    
result1 = check_palindrome(numbers1)
result2 = check_palindrome(numbers2)
    
print("List 1:", result1)
print("List 2:", result2)
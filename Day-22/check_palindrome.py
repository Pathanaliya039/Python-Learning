def is_palindrome(items):
    reversed_items = items[::-1]

    if items == reversed_items:
        return "palindrome"
    else:
        return "Not Palindrome"


items = [1, 2, 3, 2, 1]

result = is_palindrome(items)

print("Result:", result)
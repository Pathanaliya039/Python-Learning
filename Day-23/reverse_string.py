def reverse_string(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text


    return reversed_text


text = "Python"

result = reverse_string(text)

print("Reversed:", result)
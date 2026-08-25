def count_characters(text):
    count = 0

    for character in text:
        count = count + 1

    return count


text = "Python"

result = count_characters(text)

print("Characters:", result)
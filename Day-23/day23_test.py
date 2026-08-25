def count_words(text):
    count = 0
    words = text.split()

    for word in words:
        count = count + 1

    return count

text = "I am learning Python"

result = count_words(text)

print("Words:", result)
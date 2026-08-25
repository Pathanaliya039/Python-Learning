def count_vowels(text):
    count = 0

    for character in text:
        if character in "aeiouAEIOU":
            count = count + 1

    return count


text = "Hello Python"

result = count_vowels(text)

print("Vowels:", result)
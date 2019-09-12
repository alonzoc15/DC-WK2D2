word = input("Please enter a word: ")

letter_histogram = {}

for letter in word:
    keys = letter_histogram.keys()
    if letter in keys:
        letter_histogram[letter] += 1
    else:
        letter_histogram[letter] = 1

print(letter_histogram)
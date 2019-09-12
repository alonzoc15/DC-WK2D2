sentence = input("Please enter a sentence: ")
sentence_split = sentence.split(" ")

word_histogram = {}

for word in sentence_split:
    keys = word_histogram.keys()
    if word in keys:
        word_histogram[word] += 1
    else:
        word_histogram[word] = 1
        
print(word_histogram):
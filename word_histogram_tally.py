import operator
sentence_tally = input("Please enter a sentence: ")
word_histogram_tally = {}
sentence_sorted = sorted(word_histogram_tally.items(), key=operator.itemgetter(0))


for word in sentence_tally:
    keys = word_histogram_tally.keys()
    if word in keys:
        word_histogram_tally[word] += 1
    else:
        word_histogram_tally[word] = 1
        
print("your top 3 words are: ", word_histogram_tally)
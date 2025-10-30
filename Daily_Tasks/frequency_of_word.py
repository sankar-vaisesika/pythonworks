words="hello world hello python world"

words=words.split()

print(words)

word_frequency={w:words.count(w) for w in words}

print(word_frequency)


#method 2

from collections import Counter

word_frequency=dict(Counter(words))

print(word_frequency)
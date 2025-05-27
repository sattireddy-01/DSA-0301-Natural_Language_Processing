import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Sample sentence
sentence = "The bank will not approve my loan."

# Tokenize the sentence
words = word_tokenize(sentence)

# Apply the Lesk algorithm to disambiguate the word 'bank'
sense = lesk(words, "bank")

# Output the best sense
print(f"Best sense for 'bank': {sense.name()} → {sense.definition()}")

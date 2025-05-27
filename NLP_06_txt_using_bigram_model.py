import nltk
import random
from nltk.util import bigrams
from collections import defaultdict

text = "the cat sat on the mat the cat ate a rat the rat ran away"

words = text.split()

bigram_pairs = list(bigrams(words))

bigram_model = defaultdict(list)
for w1, w2 in bigram_pairs:
    bigram_model[w1].append(w2)

def generate_text(start_word, length=10):
    current_word = start_word
    sentence = [current_word]
    
    for _ in range(length - 1):
        if current_word in bigram_model:
            current_word = random.choice(bigram_model[current_word])
            sentence.append(current_word)
        else:
            break
    
    return " ".join(sentence)

# Generate sentences
print("Generated Text 1:", generate_text("the", 8))
print("Generated Text 2:", generate_text("cat", 8))
print("Generated Text 3:", generate_text("rat", 8))

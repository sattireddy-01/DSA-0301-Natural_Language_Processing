import nltk
from nltk.corpus import wordnet

# Get synsets (sets of synonyms) for a word
word = "dog"
synsets = wordnet.synsets(word)

print(f"Synsets for '{word}':")
for syn in synsets:
    print(f"- {syn.name()} → {syn.definition()}")

# Explore relationships
if synsets:
    syn = synsets[0]  # Take first synset
    print("\nHypernyms (General Category):", [h.name() for h in syn.hypernyms()])
    print("Hyponyms (Specific Types):", [h.name() for h in syn.hyponyms()])
    print("Example Usage:", syn.examples())

import spacy
from nltk.corpus import wordnet

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Function to get WordNet meaning of a noun phrase
def get_meaning(word):
    synsets = wordnet.synsets(word, pos=wordnet.NOUN)
    if synsets:
        return synsets[0].definition()  # Return the first definition
    return "Meaning not found."

# Input sentence
sentence = "The intelligent student read a fascinating book about artificial intelligence."

# Process the sentence
doc = nlp(sentence)

# Extract noun phrases
noun_phrases = [chunk.text for chunk in doc.noun_chunks]

# Display noun phrases and meanings
print("Noun Phrases and Their Meanings:")
for phrase in noun_phrases:
    words = phrase.split()
    # Get the first noun in the phrase
    main_noun = next((word for word in words if wordnet.synsets(word, pos=wordnet.NOUN)), None)
    meaning = get_meaning(main_noun) if main_noun else "Meaning not found."
    print(f"📌 {phrase}: {meaning}")

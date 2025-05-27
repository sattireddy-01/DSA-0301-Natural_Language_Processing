import spacy
import neuralcoref

# Load SpaCy model and add NeuralCoref
nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

# Input text
text = "John bought a new car. He loves it and drives it every day."

# Process the text
doc = nlp(text)

# Resolve references
resolved_text = doc._.coref_resolved

print("Original Text:")
print(text)
print("\nResolved Text:")
print(resolved_text)

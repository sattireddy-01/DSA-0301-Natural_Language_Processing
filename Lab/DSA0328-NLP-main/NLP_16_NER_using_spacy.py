import spacy

nlp = spacy.load("en_core_web_sm")

text = "Elon Musk is the CEO of Tesla, and he was born in South Africa."

doc = nlp(text)

print("Named Entities and Their Labels:")
for ent in doc.ents:
    print(f"{ent.text} → {ent.label_}")

spacy.displacy.render(doc, style="ent", jupyter=False)

from transformers import MarianMTModel, MarianTokenizer

# Define the translation model and tokenizer for English-to-French
model_name = 'Helsinki-NLP/opus-mt-en-fr'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# English text to translate
english_text = "The quick brown fox jumps over the lazy dog."

# Tokenize and translate
translated = model.generate(**tokenizer(english_text, return_tensors="pt", padding=True))
french_text = tokenizer.decode(translated[0], skip_special_tokens=True)

print("Original English Text:")
print(english_text)
print("\nTranslated French Text:")
print(french_text)

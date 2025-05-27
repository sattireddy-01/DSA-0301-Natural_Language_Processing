import nltk
from nltk.tag import UnigramTagger, DefaultTagger, brill, BrillTaggerTrainer
from nltk.corpus import treebank

# Download required data
nltk.download('treebank')

# Load training data
train_data = treebank.tagged_sents()[:3000]  # First 3000 sentences for training

# Create a Unigram Tagger as the baseline model
unigram_tagger = UnigramTagger(train_data, backoff=DefaultTagger("NN"))

# Define transformation rules
templates = [
    brill.SymmetricProximateTokensTemplate(brill.Pos([-1])),  # Look at previous word's POS
    brill.SymmetricProximateTokensTemplate(brill.Pos([1])),   # Look at next word's POS
]

# Train the Brill Tagger
trainer = BrillTaggerTrainer(unigram_tagger, templates)
brill_tagger = trainer.train(train_data, max_rules=100)

# Test sentence
test_text = "The robot quickly analyzed the data and made a decision."

# Tokenization
tokens = word_tokenize(test_text)

# Apply Brill Tagger
pos_tags = brill_tagger.tag(tokens)

# Display results
print("Word  →  POS Tag")
for word, tag in pos_tags:
    print(f"{word:10}  →  {tag}")

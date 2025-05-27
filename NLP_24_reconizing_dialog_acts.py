import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import nps_chat

# Load chat data from NLTK's corpus
nltk.download("nps_chat")
nltk.download("punkt")

# Prepare data
posts = nps_chat.xml_posts()
data = [(post.text, post.get("class")) for post in posts]

# Extract features
def extract_features(text):
    words = nltk.word_tokenize(text.lower())
    return {word: True for word in words}

# Split data into training & testing sets
train_size = int(len(data) * 0.8)
train_data = [(extract_features(text), label) for text, label in data[:train_size]]
test_data = [(extract_features(text), label) for text, label in data[train_size:]]

# Train a classifier
classifier = NaiveBayesClassifier.train(train_data)

# Test a sample conversation
test_sentences = [
    "Hello, how are you?",
    "Can you help me?",
    "I love playing video games!",
    "Why is the sky blue?"
]

# Predict dialog act
for sentence in test_sentences:
    label = classifier.classify(extract_features(sentence))
    print(f"💬 '{sentence}' → {label}")

from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "The car is fast and reliable.",
    "I love programming in Python.",
    "Python is a great programming language.",
    "My car needs a service soon."
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Compute TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert to a readable format
feature_names = vectorizer.get_feature_names_out()

# Display TF-IDF scores
print("TF-IDF Matrix:")
for doc_idx, doc in enumerate(tfidf_matrix.toarray()):
    print(f"\nDocument {doc_idx+1}:")
    for word_idx, score in enumerate(doc):
        if score > 0:  # Show only relevant terms
            print(f"{feature_names[word_idx]}: {score:.4f}")

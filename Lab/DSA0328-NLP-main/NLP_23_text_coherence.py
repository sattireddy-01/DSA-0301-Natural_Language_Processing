from sentence_transformers import SentenceTransformer, util

# Load a pre-trained BERT model for sentence similarity
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample text (you can change this)
text = [
    "Artificial intelligence is transforming the world.",
    "Deep learning is a subset of machine learning.",
    "Neural networks are used in deep learning.",
    "I like pizza with extra cheese."
]

# Compute sentence embeddings
embeddings = model.encode(text, convert_to_tensor=True)

# Measure coherence by computing average similarity between consecutive sentences
coherence_scores = []
for i in range(len(text) - 1):
    similarity = util.pytorch_cos_sim(embeddings[i], embeddings[i + 1]).item()
    coherence_scores.append(similarity)

# Calculate average coherence score
avg_coherence = sum(coherence_scores) / len(coherence_scores)

# Display results
print("Sentence Coherence Scores:", coherence_scores)
print(f"🔹 Average Coherence Score: {avg_coherence:.2f} (Higher is better)")

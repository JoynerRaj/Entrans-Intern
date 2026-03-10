from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "Artificial intelligence is transforming technology.",
    "Machine learning is a branch of AI.",
    "Football is a popular sport.",
    "Cooking requires fresh ingredients.",
    "Deep learning helps computers see images.",
    "Basketball is played worldwide."
]

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(sentences)

print("Similarity Scores:\n")

max_score = 0
pair = ()

for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):

        score = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]

        print(f"Sentence {i+1} & Sentence {j+1}: {score:.2f}")

        if score > max_score:
            max_score = score
            pair = (i, j)

print("\nMost Similar Sentences:")
print(sentences[pair[0]])
print(sentences[pair[1]])
print("Similarity Score:", round(max_score,2))
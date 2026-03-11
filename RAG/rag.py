from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load document
with open("document.txt", "r") as file:
    text = file.read()

# Step 2: Split into chunks
chunks = text.split(".")

chunks = [chunk.strip() for chunk in chunks if chunk.strip() != ""]

# Step 3: Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 4: Generate embeddings for chunks
chunk_embeddings = model.encode(chunks)

# Step 5: Ask user question
query = input("Ask a question: ")

# Convert question to embedding
query_embedding = model.encode([query])

# Step 6: Calculate similarity
similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]

# Find top 3 Sentece
top_indices = similarities.argsort()[-3:][::-1]

print("\nTop Relevant Chunks:\n")

for index in top_indices:
    print(chunks[index])
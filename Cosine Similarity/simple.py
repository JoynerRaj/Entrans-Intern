from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentence1 = input("Enter Sentence 1: ")
sentence2 = input("Enter Sentence 2: ")

sentences = [sentence1, sentence2]

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(sentences)

similarity = cosine_similarity(vectors[0], vectors[1])

print("Similarity Score:", similarity[0][0])
from database import collection

def search_documents(question):

    docs = collection.find()

    results = []

    for doc in docs:
        if question.lower() in doc["content"].lower():
            results.append(doc["content"])

    return results
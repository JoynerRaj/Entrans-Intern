from fastapi import FastAPI, UploadFile, File
from database import collection
from models import Question
from retrieval import search_documents

app = FastAPI()

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    content = await file.read()

    text = content.decode("utf-8")

    document = {
        "filename": file.filename,
        "content": text
    }

    collection.insert_one(document)

    return {"message": "Document uploaded successfully"}

@app.get("/documents")
def get_documents():

    docs = collection.find({}, {"_id": 0})

    return list(docs)

@app.post("/chat")
def chat(question: Question):

    results = search_documents(question.question)

    if len(results) == 0:
        return {"answer": "No relevant information found"}

    answer = results[0]

    return {"answer": answer}


from fastapi import FastAPI, Query, HTTPException
import json


with open("data/federal_register_processed.json", "r") as f:
    documents = json.load(f)


app = FastAPI(title="Federal Register API")


@app.get("/documents/{document_number}")
async def get_document(document_number: str):
    results = documents

    for doc in results:
        if doc["document_number"] == document_number:
            return doc
    raise HTTPException(status_code=404, detail="No documents found for that filter")


# Route 1: get the documents
@app.get("/documents")
async def get_documents(limit: int = 10, doc_type: str = None, agency: str = None):
    """Return all documents as a JSON"""
    results = documents

    if doc_type is not None:
        results = [doc for doc in documents if doc["type"] == doc_type]

    if agency:
        results = [
            doc for doc in results if agency.lower() in str(doc.get("agencies")).lower()
        ]

    limited_docs = results[:limit]
    return {"count": len(limited_docs), "documents": limited_docs}


#  Health check
@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "total_documents": len(documents)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

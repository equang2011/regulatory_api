from fastapi import FastAPI
import json


with open("data/federal_register_processed.json", "r") as f:
    documents = json.load(f)


app = FastAPI(title="Federal Register API")


# Route 1 get the documents
@app.get("/documents")
async def get_all_documents():
    """Return all documents as a JSON"""
    return {"count": len(documents), "documents": documents}


# Route 2: filter by type
@app.get("/documents/by-type/{doc_type}")
async def get_by_type(doc_type: str):
    """Filter documents by type (e.g., /documents/by-type/Notice)."""
    filtered = [d for d in documents if d["type"] == doc_type]
    return {"count": len(filtered), "documents": filtered}


# Route 3: Health check
@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "total_documents": len(documents)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

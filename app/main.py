from fastapi import FastAPI, Depends, HTTPException, Query
from database import SessionLocal
from sqlalchemy.orm import Session

from app.models import Document
from app.schemas import DocumentCreate


app = FastAPI()


def get_db():
    """Dependency: provides a database session to endpoints"""

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/documents")
def create_document(doc_data: DocumentCreate, db: Session = Depends(get_db)):
    # Create a new Document object
    new_doc = Document(
        title=doc_data.title,
        type=doc_data.type,
        document_number=doc_data.document_number,
        publication_date=doc_data.publication_date,
        ingested_date=doc_data.ingested_date,
        agencies_text=doc_data.agencies_text,
        html_url=doc_data.html_url,
        pdf_url=doc_data.pdf_url,
        public_inspection_pdf_url=doc_data.public_inspection_pdf_url,
        abstract=doc_data.abstract,
        excerpts=doc_data.excerpts,
    )

    db.add(new_doc)
    db.commit()

    db.refresh(new_doc)

    return new_doc


@app.get("/documents")
def read_documents(
    limit: int = Query(10, gt=0, le=150),
    doc_type: str = None,
    agency: str = None,
    db: Session = Depends(get_db),
):

    query = db.query(Document)

    if doc_type:
        query = query.filter(Document.type == doc_type)
    if agency:
        query = query.filter(Document.agencies_text.contains(agency))

    return query.limit(limit).all()


@app.get("/documents/{doc_id}")
def read_document(doc_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == doc_id).first()

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

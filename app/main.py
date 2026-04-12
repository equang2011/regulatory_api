from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, Query
from database import SessionLocal
from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from app.models import Document
from app.schemas import DocumentCreate

from scripts.fetch_documents import fetch_documents
from scripts.ingest_documents import run_ingestion


def fetch_and_ingest():
    fetch_documents()
    run_ingestion()


@asynccontextmanager
async def lifespan(app: FastAPI):

    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_ingest, CronTrigger(hour=18, minute=0))
    scheduler.start()

    try:
        yield
    finally:
        scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


def get_db():
    """Dependency: provides a database session to endpoints"""

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/documents-status")
def documents_status(db: Session = Depends(get_db)):

    count = db.query(Document).count()

    first_doc = db.query(Document).order_by(Document.publication_date).first()
    last_doc = db.query(Document).order_by(Document.publication_date.desc()).first()

    return {
        "total_documents": count,
        "earliest_publication_date": first_doc.publication_date if first_doc else None,
        "latest_publication_date": last_doc.publication_date if last_doc else None,
    }


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


@app.get("/search-documents")
def search_documents(q: str, db: Session = Depends(get_db)):

    search_vector = func.to_tsvector(
        "english",
        func.coalesce(Document.title, "") + " " + func.coalesce(Document.abstract, ""),
    )

    search_query = func.plainto_tsquery("english", q)

    results = (
        db.query(Document)
        .filter(search_vector.bool_op("@@")(search_query))
        .limit(15)
        .all()
    )

    return results

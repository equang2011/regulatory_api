from app.schemas import DocumentCreate
from app.models import Document
from sqlalchemy.orm import Session


def create_document(db: Session, doc_data: DocumentCreate):

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

from pydantic import BaseModel
from typing import Optional


class DocumentCreate(BaseModel):
    title: str
    type: str
    document_number: str
    publication_date: str
    ingested_date: str
    agencies_text: str

    html_url: Optional[str] = None
    pdf_url: Optional[str] = None
    public_inspection_pdf_url: Optional[str] = None

    abstract: Optional[str] = None
    excerpts: Optional[str] = None

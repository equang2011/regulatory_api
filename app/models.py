from database import Base
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Document(Base):
    __tablename__ = "document"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(300))
    type: Mapped[str] = mapped_column(String(50))
    document_number: Mapped[str] = mapped_column(String(20), unique=True)

    publication_date: Mapped[str] = mapped_column(String(20))
    ingested_date: Mapped[str] = mapped_column(String(20))
    agencies_text: Mapped[str] = mapped_column(String(500))

    html_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    pdf_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    public_inspection_pdf_url: Mapped[Optional[str]] = mapped_column(
        String(500), nullable=True
    )

    abstract: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    excerpts: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    def __repr__(self):
        return f"Document(id={self.id!r})"

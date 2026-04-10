from database import Base
from datetime import date, datetime
from typing import Optional

from sqlalchemy import String, Text, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Document(Base):
    __tablename__ = "document"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    type: Mapped[str] = mapped_column(String(50))
    document_number: Mapped[str] = mapped_column(String(20), unique=True)

    publication_date: Mapped[date] = mapped_column(Date)
    ingested_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    agencies_text: Mapped[str] = mapped_column(Text)

    html_url: Mapped[str] = mapped_column(Text, nullable=True)
    pdf_url: Mapped[str] = mapped_column(Text, nullable=True)
    public_inspection_pdf_url: Mapped[Optional[str]] = mapped_column(
        String(500), nullable=True
    )

    abstract: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    excerpts: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self):
        return f"Document(id={self.id!r})"

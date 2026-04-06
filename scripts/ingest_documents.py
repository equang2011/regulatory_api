from datetime import datetime, timezone
from database import SessionLocal

import json

from app.crud import create_document
from app.models import Document
from app.schemas import DocumentCreate

input_json = "data/federal_register_processed.json"

db = SessionLocal()

with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

    for record in data:

        check = (
            db.query(Document)
            .filter(Document.document_number == record["document_number"])
            .first()
        )
        if check:
            print(
                f"This document ({record['document_number']}) already exists in the db."
            )
            continue

        doc_data = DocumentCreate(
            title=record["title"],
            type=record["type"],
            document_number=record["document_number"],
            publication_date=record["publication_date"],
            ingested_date=datetime.now(timezone.utc).isoformat(),
            agencies_text=", ".join(record.get("agencies", [])),
            html_url=record.get("html_url"),
            abstract=record.get("abstract"),
            excerpts=record.get("excerpts"),
        )

        create_document(db, doc_data)

db.close()

from datetime import datetime, timezone
from database import SessionLocal

import json

from app.crud import create_document
from app.schemas import DocumentCreate

input_json = "data/federal_register_processed.json"

db = SessionLocal()

with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

    new_docs = []
    for record in data:

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

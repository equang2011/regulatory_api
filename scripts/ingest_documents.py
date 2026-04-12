from datetime import datetime, timezone
from database import SessionLocal
from pathlib import Path

import json

from app.crud import create_document
from app.models import Document
from app.schemas import DocumentCreate


def run_ingestion():

    date_today = datetime.today().strftime("%Y-%m-%d")

    input_path = Path("data") / f"federal_register_{date_today}.json"
    if not input_path.exists():
        print("No document to ingest.")

        return

    db = SessionLocal()
    try:

        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            cnt = 0
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
                    publication_date=datetime.strptime(
                        record["publication_date"], "%Y-%m-%d"
                    ).date(),
                    ingested_date=datetime.now(timezone.utc),
                    agencies_text=", ".join(record.get("agencies", [])),
                    html_url=record.get("html_url"),
                    abstract=record.get("abstract"),
                    excerpts=record.get("excerpts"),
                )

                create_document(db, doc_data)
                cnt += 1
                print(f"Inserted: {record['document_number']}")

            print(f"Successfully inserted {cnt} records.")
    finally:
        db.close()


if __name__ == "__main__":
    run_ingestion()

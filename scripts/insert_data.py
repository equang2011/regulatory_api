import sqlite3
import json

with open("data/federal_register_processed.json", "r") as f:
    documents = json.load(f)

conn = sqlite3.connect("federal_register.db")
cursor = conn.cursor()


inserted_count = 0

for doc in documents:
    try:
        document_number = doc.get("document_number")
        title = doc.get("title")
        doc_type = doc.get("type")
        publication_date = doc.get("publication_date")
        html_url = doc.get("html_url")
        abstract = doc.get("abstract")  # Can be None/null
        excerpts = doc.get("excerpts")  # Can be None/null

        agencies_list = doc.get("agencies", [])
        if agencies_list:
            agencies = ", ".join(agencies_list)
        else:
            agencies = None

        insert_sql = """
        INSERT INTO documents (
            document_number, title, doc_type, agencies_text, publication_date, html_url, abstract, excerpts
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_sql,
            (
                document_number,
                title,
                doc_type,
                agencies,
                publication_date,
                html_url,
                abstract,
                excerpts,
            ),
        )
        inserted_count += 1

    except Exception as e:
        print(f"Error inserting document: {doc.get('title', 'Unknown')}")
        print(f"Error: {e}")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM documents")
count = cursor.fetchone()[0]
print(f"\n✓ Successfully inserted {inserted_count} documents!")
print(f"✓ Total documents in database: {count}")

print("\n--- Sample Documents ---")
cursor.execute("SELECT document_number, title, agencies_text FROM documents LIMIT 3")
samples = cursor.fetchall()

for doc_num, title, agencies_text in samples:
    print(f"\n[{doc_num}]")
    print(f"Title: {title[:60]}...")  # First 60 chars
    print(f"Agencies: {agencies_text}")


conn.close()

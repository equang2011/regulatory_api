import sqlite3

conn = sqlite3.connect("federal_register.db")

cursor = conn.cursor()

create_table_sql = """

CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_number TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    doc_type TEXT NOT NULL,
    agencies_text TEXT,
    publication_date TEXT,
    html_url TEXT,
    pdf_url TEXT,
    public_inspection_pdf_url TEXT,
    abstract TEXT,
    excerpts TEXT
)
"""

cursor.execute(create_table_sql)
conn.commit()
conn.close()

print("Database and table created successfully!")

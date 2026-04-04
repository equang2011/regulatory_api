"""
SQLite Query Examples - Federal Register Database
Exercise 3 completion - demonstrates SQL fundamentals
"""

import sqlite3


def example_1_select_all():
    """View all documents (limited to 5)"""
    conn = sqlite3.connect("federal_register.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM documents LIMIT 5")
    results = cursor.fetchall()

    for row in results:
        print(row)

    conn.close()


def example_2_specific_columns():
    """Select only specific columns"""
    conn = sqlite3.connect("federal_register.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT document_number, title, publication_date FROM documents LIMIT 5"
    )
    results = cursor.fetchall()

    for doc_num, title, date in results:
        print(f"[{doc_num}] {title} - {date}")

    conn.close()


def example_3_filter_by_agency(agency):
    """Filter documents by exact agency match"""
    conn = sqlite3.connect("federal_register.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT document_number, title FROM documents WHERE agencies_text = ?",
        (agency,),
    )

    results = cursor.fetchall()
    print(f"Found {len(results)} documents from {agency}\n")

    for doc_num, title in results:
        print(f"[{doc_num}] {title}")

    conn.close()


def example_4_pattern_search(keyword):
    """Search titles using LIKE pattern matching"""
    conn = sqlite3.connect("federal_register.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title FROM documents WHERE title LIKE ?", (f"%{keyword}%",))

    results = cursor.fetchall()
    print(f"Found {len(results)} documents about '{keyword}'\n")

    for (title,) in results:
        print(f"- {title}")

    conn.close()


def example_5_count_by_agency():
    """Count documents per agency using GROUP BY"""
    conn = sqlite3.connect("federal_register.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT agencies_text, COUNT(*) as count
        FROM documents
        GROUP BY agencies_text
        ORDER BY count DESC
    """
    )

    results = cursor.fetchall()

    print("Documents per agency:")
    for agency, count in results:
        print(f"  {agency}: {count}")

    conn.close()


def example_6_date_filter(start_date):
    """Find documents published on or after a date"""
    conn = sqlite3.connect("federal_register.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT document_number, title, publication_date
        FROM documents
        WHERE publication_date >= ?
        ORDER BY publication_date DESC
    """,
        (start_date,),
    )

    results = cursor.fetchall()

    print(f"Documents since {start_date}:\n")
    for doc_num, title, date in results:
        print(f"{date} - [{doc_num}] {title[:50]}...")

    conn.close()


def search_documents(keyword=None, agency=None, start_date=None):
    """
    Flexible search with multiple optional filters.

    Demonstrates dynamic query building.
    """
    conn = sqlite3.connect("federal_register.db")
    cursor = conn.cursor()

    query = "SELECT document_number, title, agencies_text, publication_date FROM documents WHERE 1=1"
    params = []

    if keyword:
        query += " AND title LIKE ?"
        params.append(f"%{keyword}%")

    if agency:
        query += " AND agencies_text LIKE ?"
        params.append(f"%{agency}%")

    if start_date:
        query += " AND publication_date >= ?"
        params.append(start_date)

    query += " ORDER BY publication_date DESC"

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results


if __name__ == "__main__":
    # Test searches
    print("=== Marine + Commerce Search ===")
    results = search_documents(keyword="Marine", agency="Commerce")
    print(f"Found {len(results)} documents\n")

    for doc_num, title, agency, date in results[:5]:
        print(f"{date} - {title[:50]}...")

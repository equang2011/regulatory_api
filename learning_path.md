# Federal Register API Project - Learning Path

---

## Current Status (as of March 26, 2026)

**Completed:** Exercises 1, 2, 2.5  
**Next Up:** Phase 1-4 (Local Data Querying → FastAPI Preview)  
**Timeline:** Starting tomorrow morning  
**Files Ready:** 
- `/scripts/federal_register.py` (main pipeline)
- `/data/federal_register_response.json` (raw API)
- `/data/federal_register_processed.json` (cleaned data)

---

## Overview
**Goal:** Build foundational skills before coding the main project  
**Timeline:** Weeks 1-2 (10 hours total)  
**Approach:** Focused micro-exercises that build specific competencies  

**Why this approach?** You need reps and muscle memory on practical coding tasks (API calls, file I/O, SQL, FastAPI). These exercises give you that WITHOUT relying on LLM-generated code you don't understand.

**Framework Choice: FastAPI over Flask**
- More modern and valued in 2025 job market
- Auto-generates beautiful API documentation (free professional polish)
- Type safety with Python type hints
- Learning curve nearly identical for basic CRUD operations
- Better career investment for future projects
- Interview defense: "FastAPI is industry-standard for modern microservices"

---

## Exercise 1: Federal Register API Exploration (2 hours)

**Learning Objectives:**
- Read and understand API documentation
- Make HTTP GET requests with Python
- Parse JSON responses
- Understand query parameters and response structure

**What You'll Build:**
A simple Python script that:
1. Makes a request to the Federal Register API
2. Fetches one or more documents
3. Prints specific fields from the response (title, agency, publication date, etc.)

**Resources to Study:**
- Federal Register API docs: https://www.federalregister.gov/developers/documentation/api/v1
- Python `requests` library: https://requests.readthedocs.io/en/latest/user/quickstart/
- JSON basics (if needed): https://www.w3schools.com/python/python_json.asp

**Success Criteria:**
- [ ] You can explain what a GET request is
- [ ] You've read the Federal Register API documentation and understand the endpoints
- [ ] Your script successfully fetches data from the API
- [ ] You can print at least 3 fields from the response (e.g., title, publication_date, agency_names)
- [ ] You understand the JSON structure that comes back

**Common Concepts to Learn:**
- HTTP methods (GET, POST, etc.)
- Request headers
- Query parameters (e.g., `?per_page=20&page=1`)
- JSON structure (objects, arrays, nested data)
- API rate limits (if applicable)

**Challenge Extension (optional):**
- Add query parameters to filter results (e.g., by date range or agency)
- Handle the case where the API returns no results

**Notes & Observations:**
```


Exercise 1 - COMPLETED (March 25, 2026)

What I learned:
- Successfully made HTTP GET request to Federal Register API
- Understood JSON response structure: top-level metadata (count, total_pages, next_page_url) + results array containing document objects
- Each document has fields: title, type, abstract, document_number, publication_date, agencies (nested array), etc.
- Used .json() method to parse response
- Looped through key-value pairs with .items()

What was hard:
- Understanding nested data structures (dictionaries within lists within dictionaries)
- Remembering .keys() needs parentheses to actually call the method

How I'd explain to an interviewer:
"I built a script that fetches regulatory documents from the Federal Register API. The response has pagination metadata at the top level and an array of 20 document objects in the 'results' field. I parsed the JSON and explored the structure to understand what data is available for my database schema design."

Time spent: ~2 hours
Confidence: 7/10

Next steps: 
- Clean up output formatting
- Loop through all 20 documents (not just first one)
- Extract specific fields only (title, date, first agency)
- Move to Exercise 2 (file I/O)

Exercise 1 - COMPLETED (March 226, 2026)
Final version: Loops through all 20 documents, prints title/type/date/agency
Time: ~2.5 hours total

Notes & observations:
What I learned:
- Successfully made HTTP GET request to Federal Register API using requests.get()
- Understood JSON response structure: top-level metadata (count, total_pages, next_page_url) 
  + results array containing document objects
- Each document is a dict with fields: title, type, abstract, document_number, 
  publication_date, agencies (nested list of dicts), html_url, pdf_url, excerpts, etc.
- Used .json() method on response object to parse JSON automatically
- Looped through documents with for loops and accessed nested data with bracket notation

What was hard:
- Understanding nested data structures (dicts within lists within dicts)
- Remembering that .keys() needs parentheses to call it; understanding .items() 
  iterates both keys AND values
- Figuring out that "agencies" is a list, so I need to access [0] to get first agency, 
  then ["name"] to get the name string

How I'd explain to an interviewer:
"I built a script that makes GET requests to the Federal Register API and explores 
the response structure. The API returns paginated results with metadata at the top level 
and an array of document objects. Each document is a dict with nested data—like agencies, 
which is a list of dicts. I used bracket notation and the .items() method to explore 
and extract the data I needed. I learned that APIs often return complex nested JSON, 
and you need to understand the structure before you can use it effectively."

Key takeaway for next project:
- Always inspect a few API responses before building logic around them
- Use print(obj.keys()) and print(type(obj)) liberally while exploring
- Nested structures are common; get comfortable with indexing into them

Time spent: ~2.5 hours
Confidence: 8/10

```
---

## Exercise 2: File I/O - Save and Load JSON (1.5 hours)

**Learning Objectives:**
- Write data to files in Python
- Read data from files
- Work with JSON serialization/deserialization

**What You'll Build:**
Extend your Exercise 1 script to:
1. Save the API response to a `.json` file
2. Read the file back in
3. Parse and print data from the saved file

**Resources to Study:**
- Python file operations: https://www.w3schools.com/python/python_file_handling.asp
- `json.dump()` and `json.load()`: https://docs.python.org/3/library/json.html

**Success Criteria:**
- [ ] Your script saves API responses to a JSON file
- [ ] You can read the file back and parse it
- [ ] You understand `open()`, `read()`, `write()`, `close()` (or context managers with `with`)
- [ ] You can explain when/why you'd save API responses to files

**Common Concepts to Learn:**
- File modes: `'r'`, `'w'`, `'a'`
- Context managers (`with` statements)
- JSON serialization vs. deserialization
- File paths (relative vs. absolute)

**Challenge Extension (optional):**
- Create a function that checks if a file exists before reading it
- Save multiple API responses to separate files with timestamps in the filename

**Notes & Observations:**
```
What I learned:
- Used json.dump(obj, file_object) to save Python objects as JSON to a file
- Used json.load(file_object) to read JSON from a file back into a Python object
- Context managers (with open()) automatically close files, even if code crashes
- File modes: 'w' = write (creates/overwrites), 'r' = read (must exist)
- The indent parameter (indent=2) makes JSON human-readable
- Round-trip works: Python object → JSON file → Python object (data is identical)

What was hard:
- Initially confused json.dump() vs json.dumps() — had to remember:
  * dump() takes a file object, writes to file
  * dumps() returns a string (no file needed)
- First attempt tried passing a filepath string to json.dump() instead of file object
- Mistakenly tried to use f.write() with a list (needs to be string)

How I'd explain to an interviewer:
"I extended my API script to persist data locally. I use json.dump() to save API 
responses to files, which avoids hitting the API repeatedly and lets me work offline. 
I then use json.load() to read the data back. I learned that context managers (with 
statements) handle file closing automatically, which is safer than manual close(). 
This is a foundational skill for any data pipeline—fetching remote data, storing it 
locally, and loading it back is a pattern you use constantly."

Key takeaway for next project:
- Always use 'with' statements for file I/O
- Test round-trips: save, close, load, verify the data is identical
- JSON is a safe, standard format for storing structured data
- This local file pattern is great for development and avoiding API rate limits

Time spent: ~1.5 hours
Confidence: 8/10

Next steps:
- Create a helper function that returns all fields you care about from each document
- Add error handling: what if a field is missing from some documents?
- Save processed/cleaned data (not raw API response)

Exercise 2.5: Data Processing & Cleaning
What You Built:

process_doc() function that takes a raw API document and extracts only the fields you care about
Handles missing fields (fills with empty strings)
Special case handling for nested data (agencies list → list of agency names)
Batch processed 20 documents through this function
Saved cleaned data to a separate JSON file from raw API response

What This Teaches:

Real pipelines have a "raw" stage and a "cleaned" stage
Writing reusable functions that process individual items
Defensive programming (checking for missing fields)
Working with nested data structures
Separating concerns (raw API response file ≠ processed data file)

```

**Completion Date:** March 26, 2026

---

---

## Before Exercise 3: What You'll Do in the Next 90-120 Minutes

**Phase 1: Local Data Querying (30-40 min)**
You have clean JSON data saved to disk. Before touching a database, practice filtering 
and analyzing it in memory:
- Write functions that filter documents by agency name
- Write functions that filter by document type
- Count documents per agency, per type
- Sort documents by publication_date
- This teaches you query thinking without SQL syntax

**Phase 2: CSV Export (20-30 min)**
Take your filtered data and export to CSV format:
- Convert your list of dicts to CSV rows
- Save to a .csv file
- Open in a spreadsheet to verify structure
- This bridges file formats and prepares you for database concepts

**Phase 3: Defensive Code (20-30 min)** DONE 4/3
Add error handling throughout your pipeline:
- What if the API is down? (handle connection errors)
- What if the JSON file is corrupted? (validate before processing)
- What if there are 1000 docs instead of 20? (test with pagination)
- This teaches you to think about failure modes

**Phase 4: FastAPI Preview (optional, if time)**
Create a minimal FastAPI app that loads your processed JSON and serves it as an endpoint:
- GET /documents returns your cleaned data
- GET /documents?agency=EPA filters by agency
- No database yet—just in-memory data
- This lets you see how APIs work before adding database complexity

**Why this order before Exercise 3 (SQLite)?**
Databases are powerful but complex. By practicing queries on in-memory data first, 
you'll understand *what* you're querying before learning *how* SQL syntax works. 
You'll also have real filtered data to insert into a database, making Exercise 3 
more meaningful.

---

## Exercise 3: SQLite Basics - Schema and Queries (2 hours)

**Learning Objectives:**
- Create a SQLite database
- Define a table schema
- Insert data into a database
- Query data with SELECT statements

**What You'll Build:**
1. Create a SQLite database file
2. Define a table for storing Federal Register documents (columns: id, title, agency, publication_date, document_number, etc.)
3. Insert data from your saved JSON files (Exercise 2) into the database
4. Query the database to retrieve documents

**Resources to Study:**
- SQLite with Python: https://docs.python.org/3/library/sqlite3.html
- SQL basics: https://www.w3schools.com/sql/
- Specifically: CREATE TABLE, INSERT INTO, SELECT, WHERE clauses

**Success Criteria:**
- [X] You've created a SQLite database file (`.db`)
- [X] You've defined a table with appropriate columns and data types
- [X] You can insert rows into the table
- [ ] You can SELECT data with basic filters (e.g., WHERE agency = 'EPA')
- [ ] You understand PRIMARY KEY and data types (TEXT, INTEGER, DATE)

**Common Concepts to Learn:**
- Database connections and cursors
- SQL data types (TEXT, INTEGER, REAL, BLOB)
- Primary keys vs. foreign keys
- Parameterized queries (preventing SQL injection)
- `commit()` to save changes

**Schema Design Thinking:**
What columns should your `documents` table have? Think about:
- What data comes from the Federal Register API?
- What will you want to query by? (agency, date range, keywords?)
- What's the unique identifier? (document_number?)

**Challenge Extension (optional):**
- Add an index on a frequently-queried column (e.g., publication_date)
- Write a query that counts documents by agency

**Notes & Observations:**
```
**Notes & Observations:**

Exercise 3 - COMPLETED (April 3, 2026)

What I learned:
- Created SQLite database with proper schema (columns, data types, constraints)
- Understood connection vs cursor: conn opens file, cursor executes SQL
- conn.commit() saves changes to disk (critical!)
- Used parameterized queries (?) to prevent SQL injection
- Wrote SELECT queries with WHERE, LIKE, GROUP BY, ORDER BY
- Handled NULL values with IS NULL / IS NOT NULL
- Built dynamic queries by concatenating SQL + params list

What was hard:
- Column name mismatches between CREATE TABLE and INSERT (agencies vs agencies_text)
- Understanding that database file persists old schema even after code changes
- Remembering SQL syntax: LIKE needs %, COUNT needs GROUP BY, etc.
- Debugging: had to delete .db file and recreate when schema changed

How I'd explain to an interviewer:
"I built a SQLite database to store Federal Register documents. I designed the schema 
with appropriate data types and constraints (UNIQUE on document_number, NOT NULL on 
required fields). I wrote queries to filter, aggregate, and search the data. I learned 
the importance of parameterized queries for security and how to handle dynamic search 
criteria by building queries programmatically. This taught me SQL fundamentals that 
transfer to any relational database."

Key takeaways:
- Always use ? placeholders, never f-strings in SQL
- conn.commit() is not optional - changes don't persist without it
- Schema design matters: think about what you'll query before creating tables
- DELETE database file if schema changes during development

Files created:
- scripts/create_db.py - creates database and table
- scripts/insert_data.py - loads JSON and inserts into database  
- scripts/query_examples.py - demonstrates various SQL query patterns

Time spent: ~2 hours
Confidence: 8/10

Next: Exercise 4 (FastAPI basics)

```

---

## Exercise 4: FastAPI Basics - Routing and JSON Responses (2.5 hours)

**Learning Objectives:**
- Set up a FastAPI application
- Create HTTP endpoints (routes)
- Return JSON responses (automatic with FastAPI)
- Handle URL parameters and path parameters
- Understand automatic API documentation

**What You'll Build:**
A minimal FastAPI app with:
1. `GET /documents` - returns a hardcoded list of documents as JSON
2. `GET /documents/{id}` - returns a single document by ID (hardcoded data)
3. Test both endpoints with a browser AND explore the auto-generated docs at `/docs`

**Resources to Study:**
- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
- First Steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- Path Parameters: https://fastapi.tiangolo.com/tutorial/path-params/

**Success Criteria:**
- [ ] FastAPI is installed in your environment (`pip install fastapi uvicorn`)
- [ ] You can run a FastAPI app locally with `uvicorn`
- [ ] You've created at least 2 routes
- [ ] You can return JSON data from an endpoint (it happens automatically!)
- [ ] You understand route decorators (`@app.get()`, `@app.post()`, etc.)
- [ ] You've explored the automatic docs at `http://localhost:8000/docs`
- [ ] You can access your endpoints in a browser or with `curl`

**Common Concepts to Learn:**
- Route decorators and HTTP methods (`@app.get()`, `@app.post()`)
- Automatic JSON serialization (no `jsonify()` needed!)
- Path parameters (`{id}`)
- Running with Uvicorn (the ASGI server)
- Auto-generated Swagger UI docs at `/docs`
- Type hints (optional but recommended)

**Why FastAPI over Flask:**
- More modern (better job market fit)
- Auto-generates beautiful API documentation
- Type safety with Python type hints
- Just as easy to learn for basic CRUD operations
- Better career investment for 2025+

**Challenge Extension (optional):**
- Add query parameters (e.g., `GET /documents?agency=EPA&limit=10`)
- Use Pydantic models for type validation
- Return proper HTTP status codes (200, 404, etc.)

**Notes & Observations:**
```
Exercise 4 - COMPLETED (April 3, 2026)

What I learned:
- Created FastAPI routes with @app.get() decorators
- Handled path parameters ({document_number}) and query parameters (?limit=10)
- Used HTTPException for proper error responses (404, etc.)
- Understood automatic JSON serialization in FastAPI
- Explored auto-generated docs at /docs
- Implemented filtering logic in endpoints

What was hard:
- Understanding query params vs path params initially
- Route order matters (specific before parameterized)
- Syntax for raising HTTPException vs returning tuples

How I'd explain to an interviewer:
"I built a FastAPI application with multiple endpoints that serve Federal Register 
documents. I implemented filtering by document type and agency using query parameters, 
and single-document lookup using path parameters. I learned FastAPI's automatic 
documentation generation and type validation through Python type hints. This gave me 
hands-on experience with modern Python web frameworks."

Key takeaways:
- FastAPI makes REST APIs incredibly fast to build
- Type hints aren't just documentation - they provide validation
- Auto-generated docs (/docs) are a killer feature for development
- Query params for filtering, path params for resource identification

Files created:
- exercises/main.py - FastAPI app with document endpoints
- Production structure ready in app/ directory

Time spent: ~2 hours
Confidence: 8/10

Next: SQLAlchemy ORM integration in production app (starting April 4)

```


---

## Exercise 5: Connect FastAPI to SQLite (2 hours)

**Learning Objectives:**
- Connect a FastAPI app to a database
- Query the database from an endpoint
- Return database results as JSON

**What You'll Build:**
Modify your FastAPI app from Exercise 4 to:
1. Connect to your SQLite database (from Exercise 3)
2. Query real data from the database
3. Return it via your `/documents` endpoint

**Resources to Study:**
- FastAPI + SQL databases: https://fastapi.tiangolo.com/tutorial/sql-databases/
- SQLite with Python (same as Exercise 3): https://docs.python.org/3/library/sqlite3.html

**Success Criteria:**
- [ ] Your FastAPI app connects to your SQLite database
- [ ] The `/documents` endpoint returns real data from the database
- [ ] You can filter results (e.g., by agency or date using query parameters)
- [ ] You understand how to safely pass query parameters to SQL

**Common Concepts to Learn:**
- Database connection management in FastAPI
- Converting database rows to dictionaries/JSON
- Handling query parameters from the request
- Parameterized queries (security - prevent SQL injection)
- Dependency injection (optional advanced pattern)

**Challenge Extension (optional):**
- Add error handling for database connection failures
- Add a `GET /documents/count` endpoint that returns the total number of documents
- Use Pydantic models to define response schemas

**Notes & Observations:**
```
## Exercise 5: SQLAlchemy + FastAPI Integration (April 4, 2026)

**What I built:**
- FastAPI app with SQLAlchemy ORM integration
- POST /documents endpoint (creates documents in database)
- GET /documents endpoint (lists all documents)
- GET /documents/{id} endpoint (retrieves single document)
- Dependency injection pattern for database sessions

**Key learnings:**
- SessionLocal = vending machine for database sessions
- db.add() queues changes, db.commit() saves them
- db.refresh() gets auto-generated IDs from database
- Pydantic models validate incoming JSON
- Data persists across app restarts (proof it hit the database)

**Challenges overcome:**
- Import path issues (models.py location)
- Circular import problems (fixed with proper file structure)
- Understanding dependency injection syntax

**Confidence: 8/10**

Next session: Query filtering, error handling, or database relationships

```

---

## Post-Exercises: Self-Assessment

After completing these 5 exercises, you should feel comfortable with:
- [ ] Making HTTP requests to external APIs
- [ ] Reading and parsing JSON data
- [ ] Saving/loading data from files
- [ ] Creating and querying SQLite databases
- [ ] Building FastAPI endpoints that return JSON
- [ ] Connecting FastAPI to a database
- [ ] Understanding auto-generated API documentation

**Red Flags (if any of these are still unclear, revisit):**
- "I don't understand how FastAPI routing works"
- "I'm not sure when to use `commit()` in SQL"
- "I can't explain what type hints do in FastAPI"
- "I'm copying code without understanding it"

---

## Transition to Main Project (Week 3+)

Once you've completed these exercises, you'll be ready to build the actual Federal Register API project. The main project will combine all these skills:

**Module 1: Data Fetcher**
- Use Exercise 1 skills + add pagination handling
- Fetch multiple pages of results from the Federal Register API

**Module 2: Database Schema & Storage**
- Use Exercise 3 skills + design a production schema
- Store fetched documents in SQLite

**Module 3: API Endpoints**
- Use Exercise 4 & 5 skills + add search/filter logic
- Build endpoints: `GET /documents`, `GET /documents/<id>`, `GET /documents/search?query=...`

**Module 4: Testing & Polish**
- Write basic tests for your endpoints
- Add error handling
- Document your API

---

## How to Use This Document with LLMs

When asking for help, include this context:

```
I'm working through a structured learning path for a Federal Register API project. 
I'm currently on Exercise [NUMBER]: [EXERCISE NAME].

[Paste the relevant exercise section]

My specific question is: [YOUR QUESTION]
```

**Good LLM questions:**
- "I'm getting a KeyError when parsing the API response. Here's my code: [CODE]. What am I missing conceptually?"
- "I don't understand when to use `cursor.execute()` vs `cursor.executemany()`. Can you explain the difference?"
- "I've completed Exercise 3. Can you review my schema design? [SCHEMA]"

**Bad LLM questions:**
- "Write the code for Exercise 1" (defeats the purpose)
- "Fix this error" (without showing your code or explaining what you've tried)
- "Just give me the answer" (you won't learn)

---

## Interview Defense Builder

As you complete each exercise, write down:
1. **What you learned**
2. **One thing that was hard**
3. **How you'd explain this to an interviewer**

This will become your interview prep document.

---

## Progress Tracking

**Week 1:**
- [X] Exercise 1 (2.5 hrs) — COMPLETED
- [X] Exercise 2 (1.5 hrs) — COMPLETED  
- [X] Exercise 2.5: Data Processing & Cleaning (1 hr) — COMPLETED
- [ ] Exercise 3 (2 hrs) — NEXT

**Week 2:**
- [ ] Exercise 4 (2.5 hrs)
- [ ] Exercise 5 (2 hrs)

**Total Time Invested:** _____ hours  
**Confidence Level (1-10):** _____

---

## Final Notes

Remember: The goal is NOT to finish quickly. The goal is to **build muscle memory and understanding**. If an exercise takes longer than estimated, that's fine. Better to deeply understand Exercise 1 than to rush through all 5 with shallow knowledge.

When you're stuck, ask: "What concept am I missing?" not "What's the code?"



## Current Status (April 5, 2026)

**What's built and working:**
- FastAPI app with endpoints to create and retrieve documents
- SQLAlchemy ORM with Document model and SQLite database
- Ingest script that loads processed JSON into the database with duplicate handling
- Basic `/documents-status` endpoint showing record count and date range

**Roadmap:**

**Phase 1 (next session):** Wire in the API fetch script from Exercise 2.5 so the 
full pipeline runs end to end: Federal Register API → JSON → database

**Phase 2 (weeks 2-3):** Add Celery + Redis for scheduled weekly ingestion jobs 
so the pipeline runs automatically instead of manually

**Phase 3 (later):** Migrate from SQLite to PostgreSQL, then add pgvector for 
semantic search across documents

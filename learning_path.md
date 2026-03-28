# Federal Register API Project - Learning Path

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

Exercise 1 - COMPLETED (March 25-26, 2026)
Final version: Loops through all 20 documents, prints title/type/date/agency
Time: ~2.5 hours total
Ready for Exercise 2

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





```

**Completion Date:** ___________

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
- [ ] You've created a SQLite database file (`.db`)
- [ ] You've defined a table with appropriate columns and data types
- [ ] You can insert rows into the table
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
[Space for your own notes]




```

**Completion Date:** ___________

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
[Space for your own notes]




```

**Completion Date:** ___________

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
[Space for your own notes]




```

**Completion Date:** ___________

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
- [X] Exercise 1 (2 hrs)
- [ ] Exercise 2 (1.5 hrs)
- [ ] Exercise 3 (2 hrs)

**Week 2:**
- [ ] Exercise 4 (2.5 hrs)
- [ ] Exercise 5 (2 hrs)

**Total Time Invested:** _____ hours  
**Confidence Level (1-10):** _____

---

## Final Notes

Remember: The goal is NOT to finish quickly. The goal is to **build muscle memory and understanding**. If an exercise takes longer than estimated, that's fine. Better to deeply understand Exercise 1 than to rush through all 5 with shallow knowledge.

When you're stuck, ask: "What concept am I missing?" not "What's the code?"

Good luck! 🚀

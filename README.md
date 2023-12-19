
# Fast API books project V2


Description of the Python code:
This code defines a simple API for managing a collection of books using FastAPI and Pydantic in Python.

1. Imports:

from typing import Optional: Imports the Optional type used for specifying optional fields in models.
from fastapi import FastAPI, Path, Query, HTTPException: Imports necessary functions and classes from FastAPI to define the API endpoints and handle exceptions.
from pydantic import BaseModel, Field: Imports BaseModel and Field from Pydantic to define data models for books and requests.
2. Data Model Definitions:

Book: Represents a book with attributes like id, title, author, description, rating, and published date.
BookRequest: Defines the expected format for input data when creating or updating books. It specifies some fields as optional (Optional), and uses data validation constraints like minimum/maximum lengths and ranges.
3. Global Books List:

BOOKS: A global list containing initial book data as instances of the Book class.
4. API Endpoints:

GET /books: Retrieves all books in the BOOKS list.
GET /books/{id}: Retrieves a specific book by its ID. Raises an error if the book is not found.
GET /books/publish/{published_date}: Retrieves all books published on a specific date.
GET /books/?book_rating={book_rating}: Retrieves all books with a specific rating.
POST /books: Creates a new book based on the data provided in a BookRequest object. Assigns a new ID and adds it to the BOOKS list.
PUT /books/update_book: Updates an existing book with the data provided in a BookRequest object. Matches the book by ID and replaces it in the BOOKS list. Raises an error if the book is not found.
DELETE /books/{book_id}: Deletes a book by its ID from the BOOKS list. Raises an error if the book is not found.
5. Helper Functions:

find_book_id:** Generates a new unique ID for a new book based on the last ID in theBOOKS` list.
Overall, this code provides a basic CRUD API for managing books with validation, error handling, and data representation using models.

## Create the virtual enviroment
- python -m venv fastapienv
## Enable the enviroment
- fastapienv\Scripts\activate
## install the dependencies
- pip install requirements.txt
## Start the project
- uvicorn books:app --reload

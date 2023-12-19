from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=999)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'Miguel Sánchez',
                'description': 'A new description',
                'rating': 5,
                'published_date': 2020,
            }
        }



BOOKS = [
    Book(1, 'Title one', 'Author one', 'nice book', 5, 2000),
    Book(2, 'Title 2', 'Author one', 'great book', 4, 2012),
    Book(3, 'Title 3', 'Author 2', 'good book', 5, 2020),
    Book(4, 'Title 4', 'Author 2', 'great', 4, 2010),
]


@app.get("/books")
async def read_all_books():
    print("hola")
    return BOOKS


@app.get("/books/{id}")
async def read_book(id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404,detail="Book not found")


@app.get("/books/publish/")
async def date_book(published_date: int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.post("/books")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    new_book = find_book_id(new_book)
    BOOKS.append(new_book)
    return new_book


def find_book_id(book: Book):

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_change=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_change = True
    if not book_change:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_change = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_change = True
            break
    if not book_change:
        raise HTTPException(status_code=404, detail="Book not found")

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

DATABASE_PATH = Path(__file__).with_name("books.db")
app = FastAPI(title="Library API with SQLite")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookUpdate(BaseModel):
    title: str
    author: str


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def initialize_database() -> None:
    with get_connection() as connection:
        # TODO: Create the books table if it does not already exist.
        pass


initialize_database()


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> Book:
    with get_connection() as connection:
        # TODO: Insert the book using a parameterized query and return it.
        pass


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    with get_connection() as connection:
        # TODO: Select all books and convert each row to a Book.
        return []


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    with get_connection() as connection:
        # TODO: Select the book by ID and raise HTTPException(404) if missing.
        raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate) -> Book:
    with get_connection() as connection:
        # TODO: Update the book by ID and raise HTTPException(404) if missing.
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    with get_connection() as connection:
        # TODO: Delete the book by ID and raise HTTPException(404) if missing.
        raise HTTPException(status_code=404, detail="Book not found")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

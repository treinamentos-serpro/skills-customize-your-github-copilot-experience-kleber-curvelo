import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Library API")
books: dict[int, "Book"] = {}


class Book(BaseModel):
    # TODO: Add id, title, and author fields.
    pass


@app.get("/health")
def health_check() -> dict[str, str]:
    # TODO: Return {"status": "ok"}.
    return {"status": "todo"}


# TODO: Add POST /books and GET /books routes.
# TODO: Add GET /books/{book_id}, PUT /books/{book_id}, and DELETE /books/{book_id} routes.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

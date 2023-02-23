from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5432",
    database="books"
)


def create_book(title, writer, genre):
    cur = connection.cursor()
    cur.execute("INSERT INTO Books (title, writer, genre) VALUES (%s, %s, %s);", (title, writer, genre))
    connection.commit()
    cur.execute('SELECT LASTVAL()')
    resualt = cur.fetchone()
    cur.close()
    return resualt[0]


def show_books():
    cur = connection.cursor()
    cur.execute("SELECT * FROM Books;")
    rows = cur.fetchall()
    cur.close()
    return rows

def show_book(id):
    cur = connection.cursor()
    cur.execute("SELECT * FROM Books WHERE id = %s;", id)
    rows = cur.fetchone()
    cur.close()
    return rows


def uptade_book(title, writer, genre, id):
    cur = connection.cursor()
    cur.execute("UPDATE Books SET title=%s, writer=%s, genre=%s WHERE id = %s;", (title, writer, genre, id))
    connection.commit()
    cur.close()
    return f"Book with id {id} updated!"


def delete_book(id):
    cur = connection.cursor()
    cur.execute("DELETE FROM Books WHERE id = %s;", id)
    connection.commit()
    cur.close()
    return f"Book with id {id} deleted"


app = FastAPI()


class Books(BaseModel):
    id: str  # we can define a path for it.
    title: str
    writer: str# it explain the task of worker
    genre: str


@app.post("/books")
def create(title: str, writer: str, genre: str):
    id = create_book(title, writer, genre)
    # dict1[w.id] = w.task
    return f"The {title} by {writer} added"


@app.get("/books")
def retrieve():
    return show_books()


@app.get("/books/{id}")
def ret_id(id: str):

    if show_book(id) is None:
        return "There is no one with this id!"
    result = show_book(id)
    return f"The {result[1]} by {result[2]}"


@app.put("/books/{id}")
async def update_item(item: Books):
    if show_book(item.id) is None:
        return "There is no one with this id!"
    uptade_book(item.title, item.writer, item.genre, item.id)
    return f"The {item.id} change to {item.title}"

@app.delete("/title/{id}")
def delete_book1(id: str):
    if show_book(id) is None:
        return "There is no one with this id!"
    delete_book(id)
    return f"The Book of {id} has been deleted!"

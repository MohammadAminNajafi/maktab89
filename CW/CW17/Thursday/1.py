from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="",
    database="task"
)


def create_task(desc):
    cur = connection.cursor()
    cur.execute("INSERT INTO task (task_desc) VALUES (%s);", (desc,))
    connection.commit()
    cur.execute('SELECT LASTVAL()')
    resualt = cur.fetchone()
    cur.close()
    return resualt[0]


def show_tasks():
    cur = connection.cursor()
    cur.execute("SELECT * FROM task;")
    rows = cur.fetchall()
    cur.close()
    return rows

def show_task(id):
    cur = connection.cursor()
    cur.execute("SELECT * FROM task WHERE task_id = %s;",id)
    rows = cur.fetchone()
    cur.close()
    return rows


def uptade_task(id, desc):
    cur = connection.cursor()
    cur.execute("UPDATE task SET task_desc = %s WHERE task_id = %s;", (desc, id))
    connection.commit()
    cur.close()
    return f"task with id {id} updated!"


def delete_task(id):
    cur = connection.cursor()
    cur.execute("DELETE FROM task WHERE task_id = %s;", id)
    connection.commit()
    cur.close()
    return f"task with id {id} deleted"


app = FastAPI()


class Worker(BaseModel):
    id: str  # we can define a path for it.
    task: str  # it explain the task of worker


dict1 = {}


@app.post("/tasks")
def create(task: str):
    id = create_task(task)
    # dict1[w.id] = w.task
    return f"The {id} must {task}"


@app.get("/tasks")
def retrieve():
    return show_tasks()


@app.get("/tasks/{id}")
def ret_id(id: str):
    # if id not in dict1:
    #     return "There is no one with this id!"
    # task = dict1[id]
    if show_task(id) is None:
        return "There is no one with this id!"
    resault = show_task(id)
    return f"The {resault[0]} must {resault[1]}"


@app.put("/tasks/{id}")
async def update_item(item: Worker):
    if show_task(item.id) is None:
        return "There is no one with this id!"
    uptade_task(item.id,item.task)
    # if id not in dict1:
    #     return "There is no one with this id!"
    # update_item_encoded = item
    # dict1[id] = update_item_encoded.task
    return f"The {item.id} must {item.task}"

@app.delete("/tasks/{id}")
def delete_task1(id: str):
    if show_task(id) is None:
        return "There is no one with this id!"
    delete_task(id)
    # if id not in dict1:
    #     return "There is no one with this id!"
    # del dict1[id]
    return f"The task of {id} has been deleted!"

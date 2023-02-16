from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str = None
    number: str = None


class Person:
    contacts = {}
    def __init__(self, user: User):
        self.name = user.name
        self.number = user.number

@app.get('/signin/{name}/{number}')
def contact(name: str, number: str):
    user = User()
    user.name = name
    user.number = number
    new = Person(user)
    Person.contacts[name] = new.number
    return f'your user {name} with {number} id loggined'

@app.get('/search/{name}')
def search(name: str):
    return Person.contacts[name]

@app.get('/list')
def _list():
    return Person.contacts


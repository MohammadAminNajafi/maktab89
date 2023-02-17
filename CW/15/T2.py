from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from pydantic import BaseModel
# from fastapi.responses import HTMLResponse

jani = Jinja2Templates(directory='/home/peaman/Desktop/MANA/PEAMAN/maktab-e sharif/بوت کمپ/CW/15/')

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
def contact(name: str, number: str, requests: Request):
    user = User()
    user.name = name
    user.number = number
    new = Person(user)
    Person.contacts[name] = new.number
    return jani.TemplateResponse('signin.html', {'request': requests})

@app.get('/search/{name}')
def search(name: str):
    return Person.contacts[name]

@app.get('/list')
def _list(requests: Request):
    return jani.TemplateResponse('list.html', {'request': requests, 'contact': Person.contacts})





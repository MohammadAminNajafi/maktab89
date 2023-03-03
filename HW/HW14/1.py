
from fastapi import FastAPI, Query

app = FastAPI()

items = [
    {'fname': 'Mohammad', 'lname': 'Pedrami'},
    {'fname': 'MohammadAmin', 'lname': 'Najafi'}
]

@app.get('/search')
def search(term: str = Query(None, min_length=1)):
    results = [item for item in items if term.lower() in item['fname'].lower() or term.lower() in item['lname'].lower()]
    return results
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/response')
def error_handler():
    raise HTTPException(status_code=500, detail='Error Handler')






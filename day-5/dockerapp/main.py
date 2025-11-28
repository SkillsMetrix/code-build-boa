from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def loadUsers():
    return {"message":" welcome to FastAPI"}
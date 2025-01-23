from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def helloWorld():
    return "Hello World" 
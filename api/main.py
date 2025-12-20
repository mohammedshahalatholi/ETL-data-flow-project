from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    listdata=[3,345,75,5,5,231,5635,132,123,75,4,2,67,879,343,797,232,85,32,545,775,234]
    return listdata


@app.get("/hello/{name}")
def say_hello(name):
    return {"greeting": f"Hello {name}"}


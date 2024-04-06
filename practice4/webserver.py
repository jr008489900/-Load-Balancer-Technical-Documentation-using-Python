from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def read_test():
    return {
        "message": "Hello, this is JSON data from FASTAPI!",
        "data": {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
    }
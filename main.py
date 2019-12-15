from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_world():
    """
    Root view, returns {'hello': 'world'}
    """
    return{'hello': 'world'}
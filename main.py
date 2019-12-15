from fastapi import FastAPI
from todo import router

app = FastAPI()


@app.get('/')
def hello_world():
    """
    Root view, returns {'hello': 'world'}
    """
    return{'hello': 'world'}


app.include_router(router, prefix='/list', tags=['list'])

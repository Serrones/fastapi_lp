from data import ToDoList
from models import ItemModel

from fastapi import FastAPI
from typing import List, Dict, Any, Optional


app = FastAPI()

todo_list = ToDoList()


@app.get('/')
def hello_world():
    """
    Root view, returns {'hello': 'world'}
    """
    return{'hello': 'world'}

@app.get('/list', response_model=List[ItemModel])
def list_todo():
    """
    View returns todo list
    """
    return todo_list.get_all()


@app.post('/list', response_model=ItemModel, status_code=201)
def insert_todo(item: ItemModel):
    """
    View that inserts an item in todo list
    """
    return todo_list.insert_item(item.dict())
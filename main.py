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
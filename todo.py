from data import ToDoList, StatusOptions
from models import ItemModel, ItemResponseModel
from typing import List, Dict, Any, Optional

from fastapi import APIRouter

router = APIRouter()

todo_list = ToDoList()


@router.get('/', response_model=List[ItemResponseModel])
def list_todo(status: Optional[StatusOptions]= None):
    """
    View returns todo list
    """
    if status is not None:
        return todo_list.filter_tasks(status)

    return todo_list.get_all()


@router.post('/', response_model=ItemResponseModel, status_code=201)
def insert_todo(item: ItemModel):
    """
    View that inserts an item in todo list
    """
    return todo_list.insert_item(item.dict())


@router.get('/{item_id}', response_model=ItemResponseModel)
def get_item(item_id:int):
    """
    View that gets an specific item by id
    """
    return todo_list.get_item(item_id)
from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()

todo: List[Dict[str, Any]] = [    
    {
        'id': 1,
        'title': 'FastApi',
        'description': 'Explore FastApi application',
        'status': 'doing'
    },
    {
        'id': 2,
        'title': 'AIOHTTP',
        'description': 'Explore Async concepts with AIOHTTP',
        'status': 'to do'
    }
]

@app.get('/')
def hello_world():
    """
    Root view, returns {'hello': 'world'}
    """
    return{'hello': 'world'}

@app.get('/list')
def list_todo():
    """
    View returns todo list
    """
    return todo   
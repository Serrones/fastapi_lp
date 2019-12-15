from typing import List, Dict, Any
from enum import Enum

class StatusOptions(str, Enum):
    todo = "todo"
    doing = "doing"
    done = "done"

class ToDoList:
    todo: List[Dict[str, Any]] = [    
        {
            'id': 1,
            'title': 'FastApi',
            'description': 'Explore FastApi application',
            'status': StatusOptions.doing
        },
        {
            'id': 2,
            'title': 'AIOHTTP',
            'description': 'Explore Async concepts with AIOHTTP',
            'status': StatusOptions.todo
        }
    ]

    id_now = 2
    
    def get_all(self):
        return self.todo
    
    def insert_item(self, item:Dict[str, Any])-> Dict[str, Any]:
        self.id_now += 1
        item['id'] = self.id_now
        self.todo.append(item)
        return item

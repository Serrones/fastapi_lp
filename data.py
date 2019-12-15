from typing import List, Dict, Any, Union
from enum import Enum


class StatusOptions(str, Enum):
    todo = "todo"
    doing = "doing"
    done = "done"

ITEM = Dict[str,Union[int,str, StatusOptions]]

class ToDoList:
    todo: List[Dict[str, ITEM]] = [    
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

    def get_item(self, item_id: int) -> ITEM:
        item = filter(lambda x: x['id'] == item_id, self.todo)
        return list(item)[0]

    def filter_tasks(self, status: StatusOptions) -> List[ITEM]:
        return list(filter(lambda x: x['status'] == status, self.todo))

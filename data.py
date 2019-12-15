from typing import List, Dict, Any

class ToDoList:
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

    id_now = 3
    
    def get_all(self):
        return self.todo
    
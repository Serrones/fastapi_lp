from typing import Optional

from pydantic import BaseModel



class ItemModel(BaseModel):
    id: int
    title: str
    description: str
    status: Optional[str]

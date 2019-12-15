from typing import Optional

from pydantic import BaseModel



class ItemModel(BaseModel):
    title: str
    description: str
    status: Optional[str]

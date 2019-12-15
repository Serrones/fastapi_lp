from typing import Optional

from pydantic import BaseModel

from data import StatusOptions

class ItemModel(BaseModel):
    title: str
    description: str
    status: Optional[StatusOptions]

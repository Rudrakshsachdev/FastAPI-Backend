from pydantic import BaseModel

from typing import Optional

class CreateTodo(BaseModel):
    content: str
    is_completed: bool = False
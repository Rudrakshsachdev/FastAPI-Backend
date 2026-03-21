from pydantic import BaseModel, Field

from typing import Optional

class CreateTodo(BaseModel):
    content: str = Field(
        ...,
        description="The content of the todo item",
        example="Buy groceries",
        min_length=1,
        max_length=5
    )
    is_completed: bool = False
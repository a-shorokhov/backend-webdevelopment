from pydantic import BaseModel, Field

class TaskIn(BaseModel):
    title: str
    priority: int = Field(default=1, ge=1, le=5)
    completed: bool = Field(default=False)

class TaskUpdate(BaseModel):
    title: str
    priority: int = Field(default=1, ge=1, le=5)
    completed: bool = Field(default=False)
from pydantic import BaseModel

class Status(BaseModel):
    status: str = "OK"
    description: str = "Проект на FastAPI"
    data: str = "DATA"
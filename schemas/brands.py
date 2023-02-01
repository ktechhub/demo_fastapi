from pydantic import BaseModel


class Brand(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
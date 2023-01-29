from pydantic import BaseModel
from typing import Optional


class Serie_Schema(BaseModel):
    id: Optional[int] = None
    title: str
    genre: str
    year: int
    qnt_seasons: int

    class Config:
        orm_mode = True
from datetime import date
from enum import Enum
from pydantic import BaseModel, model_validator
from sqlmodel import SQLModel, Field

class GenreURLChoices(Enum):
    ROCK = "rock"
    ELECTRONIC = "electronic"
    METAL = "metal"
    HIP_HOP = "hip-hop"

class GenreChoices(Enum):
    ROCK = "Rock"
    ELECTRONIC = "Electronic"
    METAL = "Metal"
    HIP_HOP = "Hip-Hop"

class AlbumBase(SQLModel):
    title: str
    release_date: date

class Album(AlbumBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
class BandBase(BaseModel):
    # id: int
    name: str
    genre: str
    albums: list[Album] = []

class BandCreate(BandBase):
    pass    

class BandWithID(BandBase):
    id: int

    
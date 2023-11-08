from pydantic import BaseModel


# Song Base
class SongBase(BaseModel):
    duration: float
    name: str


# Song OUT
class Song(SongBase):
    id: int
    album_id: int

    class Config:
        orm_mode = True


# Song IN
class SongCreate(SongBase):
    pass


# Album Base
class AlbumBase(BaseModel):
    duration: float
    amount_of_songs: int
    release_date: int
    name: str


# Album OUT
class Album(AlbumBase):
    band_id: int
    id: int
    songs: list[Song] = []

    class Config:
        orm_mode = True


# Album IN
class AlbumCreate(AlbumBase):
    pass


# Band Base
class BandBase(BaseModel):
    name: str
    is_still_active: bool
    lead_singer: str
    genre: str


# Band OUT
class Band(BandBase):
    id: int
    albums: list[Album] = []

    class Config:
        orm_mode = True


# Band IN
class BandCreate(BandBase):
    pass


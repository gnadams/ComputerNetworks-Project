from pydantic import BaseModel


class ItemBase(BaseModel): # class for storing bandwidth
    error: bool
    upload: float
    download: float
    time: str
    

class Item(ItemBase):
   id: int
   class Config:
      orm_mode = True



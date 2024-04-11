from typing import List, Optional

from lin import BaseModel

class KamiaddSchema(BaseModel):
    kamitime: int
    introduce: str

class KamicheckSchema(BaseModel):
    codeNumder: str
    networkCard: str
class getKamilistSchema(BaseModel):
    currentPage: int
    pageSize: int

class getKamiUserSchema(BaseModel):
    codeNumderid: int

class updatekamistatusSchema(BaseModel):
    status: int
from datetime import datetime
from pydantic import BaseModel

#TODO id при создании события не нужен т.к. он создается сам в базе, при этом это поле зачем-то является обязательным при создании
#TODO его нужно делать либо необязательным, либо например делать две разные схемы для создания и возврата событий
class EventsShema(BaseModel):
    id: str
    title: str
    description: str
    datetime: datetime

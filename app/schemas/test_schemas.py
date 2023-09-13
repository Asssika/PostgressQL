from datetime import datetime
from pydantic import BaseModel


class EventsShema(BaseModel):
    id: str
    title: str
    description: str
    datetime: datetime

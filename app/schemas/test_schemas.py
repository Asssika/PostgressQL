from datetime import datetime
from pydantic import BaseModel


class EventsShema(BaseModel):
    id: str
    title: str
    description: str
    datetime: datetime


class ProfilesShema(BaseModel):
    Number: int
    Name: str
    Login: str
    Password: str
    Pass: int
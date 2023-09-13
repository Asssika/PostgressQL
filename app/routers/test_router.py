from fastapi import APIRouter

from app.libs.handles.test_handler import create_event, get_events
from app.schemas.test_schemas import EventsShema

test_router = APIRouter()

@test_router.get('/events')
async def get_events_route():
    result = await get_events()
    return result

@test_router.post('/event')
async def create_events_route(event: EventsShema):
    result = await create_event(event=event)
    return result

@test_router.put('/event')
async def change_event_route():
    pass

@test_router.delete('/event')
async def delete_event_route():
    pass
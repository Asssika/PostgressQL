from fastapi import APIRouter

from app.libs.handles.test_handler import create_event, get_events, create_profile, get_profile
from app.schemas.test_schemas import EventsShema, ProfilesShema

test_router = APIRouter()

@test_router.get('/events')
async def get_events_route():
    result = await get_events()
    return result
async def get_profile_route():
    result = await get_profile()
    return result

@test_router.post('/event')
async def create_events_route(event: EventsShema):
    result = await create_event(event=event)
    return result

async def create_profile_route(profile: ProfilesShema):
    result = await create_profile(event=profile)
    return result

@test_router.put('/event')
async def change_event_route():
    pass

@test_router.delete('/event')
async def delete_event_route():
    pass
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.schemas.test_schemas import EventsShema
from app.setting import get_settings
from app.libs.postgres.models import Events

settings = get_settings()


connection = f'postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASS}@localhost/{settings.POSTGRESQL_DB}'
engine = create_async_engine(connection, echo=True)
asynс_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_event(event: EventsShema) -> Events:
    async with asynс_session() as session:
        new_event = Events(title=event.title,
                           description=event.description,
                           datetime=event.datetime.replace(tzinfo=None))
        session.add(new_event)
        await session.commit()

        return new_event

#TODO исправить ошибку получения событий
async def get_events() -> List[Events]:
    async with asynс_session() as session:
        stmt = select(Events)
        result = await session.execite(stmt)
        events = result.scalars().all()
        return events

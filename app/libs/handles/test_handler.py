from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.schemas.test_schemas import EventsShema, ProfilesShema
from app.setting import get_settings
from app.libs.postgres.models import Events, Profiles

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


async def get_events() -> List[Events]:
    async with asynс_session() as session:
        stmt = select(Events)
        result = await session.execite(stmt)
        events = result.scalars().all()
        return events

async def create_profile(profile: ProfilesShema) -> Profiles:
    async with asynс_session() as session:
        new_profile = Profiles(Name=profile.Name,
                           Login=profile.Login,
                           Password=profile.Password,
                           Number=profile.Number,
                           Pass=profile.Pass)
        session.add(new_profile)
        await session.commit()

        return new_profile


async def get_profile() -> List[Profiles]:
    async with asynс_session() as session:
        stmt = select(Profiles)
        result = await session.execite(stmt)
        profiles = result.scalars().all()
        return profiles
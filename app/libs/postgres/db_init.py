from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base

if __name__ == '__main__':

    CONNECTION = 'postgresql+psycopg2://postgres:123qwe@localhost/testdb'
    engine = create_engine(CONNECTION)
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.commit()

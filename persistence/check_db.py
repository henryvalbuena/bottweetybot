from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

from persistence.model import Base, Tweet


def db_init():
    db_path = "sqlite:///tweets.db"
    engine = create_engine(db_path)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    try:
        session.query(Tweet).all()
    except OperationalError:
        Base.metadata.create_all(engine)
    finally:

        return session

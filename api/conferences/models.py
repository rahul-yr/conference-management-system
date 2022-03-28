from datetime import date
from sqlalchemy import Table, Column, Integer, String, Date, DateTime, ForeignKey
# from api.config.database import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# create a table for conferences
class Conference(Base):
    __tablename__ = 'conferences'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)


class Talk(Base):
    __tablename__ = 'talks'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    duration = Column(Integer, nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    conference_id = Column(Integer, ForeignKey('conferences.id'))


class Speakers(Base):
    __tablename__ = 'speakers'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    talk_id = Column(Integer, ForeignKey('talks.id'))


class Participants(Base):
    __tablename__ = 'participants'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    talk_id = Column(Integer, ForeignKey('talks.id'))

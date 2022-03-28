from datetime import date, datetime
from pydantic import BaseModel

# conferences


class CreateConference(BaseModel):
    title: str
    description: str
    start_date: date
    end_date: date

    class Config:
        orm_mode = True


class UpdateConference(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class ViewConference(BaseModel):
    id: int
    title: str
    description: str
    start_date: date
    end_date: date

    class Config:
        orm_mode = True


# talks
class CreateTalk(BaseModel):
    title: str
    description: str
    duration: int
    start_datetime: datetime
    conference_id: int

    class Config:
        orm_mode = True


class UpdateTalk(BaseModel):
    id: int
    title: str
    description: str
    duration: int
    start_datetime: datetime
    conference_id: int

    class Config:
        orm_mode = True


class ViewTalk(BaseModel):
    id: int
    title: str
    description: str
    duration: int
    start_datetime: datetime
    conference_id: int

    class Config:
        orm_mode = True


# Speakers
class CreateSpeaker(BaseModel):
    username: str
    email: str
    talk_id: int

    class Config:
        orm_mode = True


class ViewSpeaker(BaseModel):
    id: int
    username: str
    email: str
    talk_id: int

    class Config:
        orm_mode = True

# Participants


class CreateParticipant(BaseModel):
    username: str
    email: str
    talk_id: int

    class Config:
        orm_mode = True


class ViewParticipant(BaseModel):
    id: int
    username: str
    email: str
    talk_id: int

    class Config:
        orm_mode = True

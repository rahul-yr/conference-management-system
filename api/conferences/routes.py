from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.config.database import get_db_instance
from api.conferences import crud
from api.conferences import schemas
from fastapi import responses

users_router = APIRouter()

# conferences


@users_router.post("/conferences/create", response_model=schemas.ViewConference)
async def create_conference(conference: schemas.CreateConference, db: Session = Depends(get_db_instance)):
    return crud.create_conference(db=db, conference=conference)


@users_router.get("/conferences/all", response_model=list[schemas.ViewConference])
async def get_all_conferences(db: Session = Depends(get_db_instance)):
    return crud.get_all_conferences(db)


@users_router.put("/conferences/update", response_model=schemas.ViewConference)
async def update_conference(conference: schemas.UpdateConference, db: Session = Depends(get_db_instance)):
    return crud.update_conference(db=db, conference=conference)

# talks


@users_router.get("/talk/all", response_model=list[schemas.ViewTalk])
async def get_all_talks(db: Session = Depends(get_db_instance)):
    return crud.get_all_talks(db)


@users_router.post("/talk/create", response_model=schemas.ViewTalk)
async def create_talk(talk: schemas.CreateTalk, db: Session = Depends(get_db_instance)):
    return crud.create_talk(db=db, talk=talk)


@users_router.put("/talk/update", response_model=schemas.ViewTalk)
async def update_talk(talk: schemas.UpdateTalk, db: Session = Depends(get_db_instance)):
    return crud.update_talk(db=db, talk=talk)

# speakers and participants


@users_router.get("/talk/speakers/{id}", response_model=list[schemas.ViewSpeaker])
async def get_all_speakers(id: int, db: Session = Depends(get_db_instance)):
    return crud.get_all_speakers(db=db, talk_id=id)


@users_router.get("/talk/participants/{id}", response_model=list[schemas.ViewParticipant])
async def get_all_participants(id: int, db: Session = Depends(get_db_instance)):
    return crud.get_all_participants(db=db, talk_id=id)

# add a speaker


@users_router.post("/talk/addspeaker", response_model=schemas.ViewSpeaker)
async def add_speaker(speaker: schemas.CreateSpeaker, db: Session = Depends(get_db_instance)):
    return crud.add_speaker(db=db, speaker=speaker)


@users_router.delete("/talk/deletespeaker/{id}", responses={
    200: {"message": "Successfully deleted"},
    404: {"error": "Speaker not found"},
    500: {"error": "Internal server error"}
})
async def delete_speaker(id: int, db: Session = Depends(get_db_instance)):
    return crud.delete_speaker(db=db, speaker_id=id)


@users_router.post("/talk/addparticipant", response_model=schemas.ViewParticipant)
async def add_participant(participant: schemas.CreateParticipant, db: Session = Depends(get_db_instance)):
    return crud.add_participant(db=db, participant=participant)


@users_router.delete("/talk/deleteparticipant/{id}", responses={
    200: {"message": "Successfully deleted"},
    404: {"error": "Participant not found"},
    500: {"error": "Internal server error"}
})
async def delete_participant(id: int, db: Session = Depends(get_db_instance)):
    return crud.delete_participant(db=db, participant_id=id)

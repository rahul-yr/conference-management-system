from datetime import timedelta
from sqlalchemy.orm import Session
from api.conferences.models import Conference, Talk, Speakers, Participants
from api.conferences import schemas
from fastapi.responses import JSONResponse
import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# conferences
def get_all_conferences(db: Session) -> list[Conference]:
    try:
        return db.query(Conference).all()
    except Exception as e:
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def create_conference(db: Session, conference: schemas.CreateConference) -> Conference:
    try:
        # perform the validations
        if conference.start_date <= conference.end_date:
            # create the conference
            new_conference = Conference(
                title=conference.title,
                description=conference.description,
                start_date=conference.start_date,
                end_date=conference.end_date
            )
            db.add(new_conference)
            db.commit()
            db.refresh(new_conference)
            return new_conference
        else:
            response = JSONResponse(
                {"error": "Start date must be before end date"}, media_type="application/json", status_code=400)
            return response
    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def update_conference(db: Session, conference: schemas.UpdateConference) -> Conference:
    try:
        db_conference = db.query(Conference).get(conference.id)
        if db_conference:
            db_conference.title = conference.title
            db_conference.description = conference.description
            # add updates
            db.add(db_conference)
            db.commit()
            db.refresh(db_conference)
            return db_conference
        else:
            response = JSONResponse(
                {"error": "Conference not found"}, media_type="application/json", status_code=404)
            return response
    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


# talks
def get_all_talks(db: Session, conference_id: int) -> list[Talk]:
    try:
        return db.query(Talk).filter(Talk.conference_id == conference_id).all()
    except Exception as e:
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def create_talk(db: Session, talk: schemas.CreateTalk) -> Talk:
    try:
        # get the conference
        db_conference = db.query(Conference).get(talk.conference_id)
        if db_conference and (talk.start_datetime.date() >= db_conference.start_date) and ((talk.start_datetime + timedelta(minutes=talk.duration)).date()) <= (db_conference.end_date):
            # create the talk
            new_talk = Talk(
                title=talk.title,
                description=talk.description,
                duration=talk.duration,
                start_datetime=talk.start_datetime,
                conference_id=talk.conference_id
            )
            db.add(new_talk)
            db.commit()
            db.refresh(new_talk)
            return new_talk
        else:
            response = JSONResponse(
                {"error": "Conference not found"}, media_type="application/json", status_code=404)
            return response

    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def update_talk(db: Session, talk: schemas.UpdateTalk) -> Talk:
    try:
       # get the confernce
        db_conference = db.query(Conference).get(talk.conference_id)
        if db_conference:
            db_talk = db.query(Talk).get(talk.id)
            if db_talk and (talk.start_datetime.date() >= db_conference.start_date) and ((talk.start_datetime + timedelta(minutes=talk.duration)).date()) <= (db_conference.end_date):
                db_talk.title = talk.title
                db_talk.description = talk.description
                db_talk.duration = talk.duration
                db_talk.start_datetime = talk.start_datetime
                db_talk.conference_id = talk.conference_id
                db.add(db_talk)
                db.commit()
                db.refresh(db_talk)
                return db_talk
            else:
                response = JSONResponse(
                    {"error": "Please verify details"}, media_type="application/json", status_code=404)
                return response
        else:
            response = JSONResponse(
                {"error": "Conference not found"}, media_type="application/json", status_code=404)
            return response
    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


# Speaker
def get_all_speakers(db: Session, talk_id: int) -> list[Speakers]:
    try:
        return db.query(Speakers).filter(Speakers.talk_id == talk_id).all()
    except Exception as e:
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def add_speaker(db: Session, speaker: schemas.CreateSpeaker) -> Speakers:
    try:
        username = speaker.username
        username = username.lower().strip()
        email = speaker.email.strip().lower()
        if len(username) > 2 and re.fullmatch(email_regex, email):
            # get the talk
            db_talk = db.query(Talk).get(speaker.talk_id)
            if db_talk:
                # create the speaker
                new_speaker = Speakers(
                    username=username,
                    email=email,
                    talk_id=speaker.talk_id
                )
                db.add(new_speaker)
                db.commit()
                db.refresh(new_speaker)
                return new_speaker
            else:
                response = JSONResponse(
                    {"error": "Talk not found"}, media_type="application/json", status_code=404)
                return response
        else:
            response = JSONResponse(
                {"error": "Please verify details i.e username <= 2 chars or invalid email"}, media_type="application/json", status_code=400)
            return response
    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def delete_speaker(db: Session, speaker_id: int) -> JSONResponse:
    try:
        db_speaker = db.query(Speakers).get(speaker_id)
        if db_speaker:
            db.delete(db_speaker)
            db.commit()
            response = JSONResponse(
                {"message": "Speaker deleted"}, media_type="application/json", status_code=200)
            return response
        else:
            response = JSONResponse(
                {"error": "Speaker not found"}, media_type="application/json", status_code=404)
            return response
    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response

# participants


def get_all_participants(db: Session, talk_id: int) -> list[Participants]:
    try:
        return db.query(Participants).filter(Participants.talk_id == talk_id).all()
    except Exception as e:
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def add_participant(db: Session, participant: schemas.CreateParticipant) -> Participants:
    try:
        username = participant.username
        username = username.lower().strip()
        email = participant.email.strip().lower()
        if len(username) > 2 and re.fullmatch(email_regex, email):
            # get the talk
            db_talk = db.query(Talk).get(participant.talk_id)
            if db_talk:
                # create the participant
                new_participant = Participants(
                    username=username,
                    email=email,
                    talk_id=participant.talk_id
                )
                db.add(new_participant)
                db.commit()
                db.refresh(new_participant)
                return new_participant
            else:
                response = JSONResponse(
                    {"error": "Talk not found"}, media_type="application/json", status_code=404)
                return response
        else:
            response = JSONResponse(
                {"error": "Please verify details i.e username <= 2 chars or invalid email"}, media_type="application/json", status_code=400)
            return response
    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response


def delete_participant(db: Session, participant_id: int) -> JSONResponse:
    try:
        db_participant = db.query(Participants).get(participant_id)
        if db_participant:
            db.delete(db_participant)
            db.commit()
            response = JSONResponse(
                {"message": "Participant deleted"}, media_type="application/json", status_code=200)
            return response
        else:
            response = JSONResponse(
                {"error": "Participant not found"}, media_type="application/json", status_code=404)
            return response
    except Exception as e:
        db.rollback()
        response = JSONResponse(
            {"error": "Something went wrong"}, status_code=500)
        return response

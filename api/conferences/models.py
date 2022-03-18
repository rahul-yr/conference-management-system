from app import db
from datetime import date

# create a table for conferences


class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Conference %r>' % self.title


# create a table for talks
class Talk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_datetime = db.Column(db.DateTime, nullable=False)
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))

    def __repr__(self):
        return '<Talk %r>' % self.title


# create a table for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# create a table for speakersList


# class Speaker(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # create a field talk_id
#     talk_id = db.Column(db.Integer, db.ForeignKey('talk.id'))
#     # create a field of type list of users
#     users = db.relationship(
#         'User', secondary='speaker_user', backref='speakers')

#     def __repr__(self):
#         return '<Speaker %r>' % self.id.username


# # create a table for participants
# class Participant(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # create a field talk_id
#     talk_id = db.Column(db.Integer, db.ForeignKey('talk.id'))
#     # create a field of type list of users
#     users = db.relationship(
#         'User', secondary='participant_user', backref='participants')

#     def __repr__(self):
#         return '<Participant %r>' % self.id.username

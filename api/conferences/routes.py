from flask import Flask, request, jsonify
from api.conferences.models import Conference
from app import db
from datetime import datetime


def create():
    input_object = request.json
    if input_object is None:
        return jsonify({"message": "No input object"}), 400
    if "title" not in input_object:
        return jsonify({"message": "Missing title"}), 400
    if "description" not in input_object:
        return jsonify({"message": "Missing description"}), 400
    if "start_date" not in input_object:
        return jsonify({"message": "Missing start_date"}), 400
    if "end_date" not in input_object:
        return jsonify({"message": "Missing end_date"}), 400

    start_date = datetime.strptime(input_object['start_date'], '%d-%m-%Y')
    input_object['start_date'] = start_date
    end_date = datetime.strptime(input_object['end_date'], '%d-%m-%Y')
    input_object['end_date'] = end_date

    if input_object["start_date"] > input_object["end_date"]:
        return jsonify({"message": "Invalid start_date"}), 400

    conference = Conference(
        title=input_object['title'],
        description=input_object['description'],
        start_date=input_object['start_date'],
        end_date=input_object['end_date']
    )
    # save the conference
    db.session.add(conference)
    db.session.commit()
    # return the conference
    return jsonify(conference.serialize())


def generate_conference_routes(app: Flask):
    app.add_url_rule(
        rule='/api/conferences/create',
        view_func=create,
        methods=['POST']
    )

from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# load env files
load_dotenv('.dev.env')
app = Flask(__name__)
# configure env variables
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')
app.config['DEBUG'] = environ.get('DEBUG', False)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


def init_routes(app: Flask):
    from api.conferences.routes import generate_conference_routes
    generate_conference_routes(app)


if __name__ == "__main__":
    init_routes(app)
    app.run()
    # app.run(debug=app.config['DEBUG'])

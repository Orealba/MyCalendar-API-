import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from flask import Flask
from flask_restful import Api

from api_Calendar.constants import PROJECT_ROOT, API_CALENDAR_DATABASE
from api_Calendar.database import db 
from api_Calendar.resources.eventResources import EventResource, EVENTS_ENDPOINT

def create_app(db_location):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("events.log"), logging.StreamHandler()],
    )

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(app)

    api = Api(app)
    api.add_resource(EventResource, EVENTS_ENDPOINT, f"{EVENTS_ENDPOINT}/<id>")
    return app

if __name__ == "__main__":
    app = create_app(f"sqlite:////{PROJECT_ROOT}/{API_CALENDAR_DATABASE}")
    app.run(debug=True)

   



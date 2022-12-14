import logging
import sys
from os import path
from flask import Flask
from flask_restful import Api
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from api_Calendar.constants import PROJECT_ROOT, API_CALENDAR_DATABASE, FRONT_URL
from api_Calendar.database import db 
from api_Calendar.resources.eventResources import EventResource, EVENTS_ENDPOINT 
from flask_cors import CORS



def create_app(db_location):
    #log configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("events.log"), logging.StreamHandler()],
    )

    app = Flask(__name__)
    #allow frontend call
    cors = CORS(app, resources={r"/api/*": {"origins": FRONT_URL}})

    #initialize datebase
    app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(app)

    #create the api and add the resource
    api = Api(app)
    api.add_resource(EventResource, EVENTS_ENDPOINT, f"{EVENTS_ENDPOINT}/<id>")
    return app

    #create the app and run it
if __name__ == "__main__":
    app = create_app(f"sqlite:////{PROJECT_ROOT}/{API_CALENDAR_DATABASE}")
    app.run(host='0.0.0.0', debug=True)

   



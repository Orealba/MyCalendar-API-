import logging
from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from api_Calendar.database import db
from api_Calendar.models.events import Event
from api_Calendar.schemas.eventSchema import EventSchema


EVENTS_ENDPOINT = "/api/events"
logger = logging.getLogger(__name__)

class EventResource (Resource) :
    def get (self, id=None):
        if not id:
            logger.info(
                f"All events were successfully retrieved"
            )
            return self._get_all_events(), 200

        logger.info(f"The event was successfully retrieved by id {id}")
        try:
            return self._get_event_by_id(id), 200
        except NoResultFound:
            abort(404, message="event not found, try again")

    def _get_event_by_id(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        event_json = EventSchema().dump(event)

        if not event_json:
            raise NoResultFound()

        logger.info(f"Event retrieved from database {event_json}")
        return event_json


    def _get_all_events(self):
        
        events = Event.query.all()

        events_json = [EventSchema().dump(event) for event in events]

        logger.info("Events successfully retrieved.")
        return events_json

    def post(self):
        req = request.get_json()

        if (req["title"] == "" or req["description"] == ""  or req["start_date"] == "" or req["end_date"] == "" or 
            req["title"] == None or req["description"] == None  or req["start_date"] == None or req["end_date"] == None):
            
            return abort(400, message="fill all fields")
        event = EventSchema().load(request.get_json())
        try:
            db.session.add(event)
            db.session.commit()
        except IntegrityError as e:
            logger.warning(
                f"Integrity Error, this event is already in the database. Error: {e}"
            )

            abort(409, message="Unexpected Error!")
        else:
            return event.id, 201

    def delete (self,id):
        try:
            event = Event.query.filter_by(id=id).first()
            if not event:
                raise NoResultFound()

            db.session.delete(event)
            db.session.commit()
            logger.info("Events successfully deleted.")
            return "", 204

        except NoResultFound:
            abort(404, message="event not found")    

        
    def put (self,id):
        reqput = request.get_json()

        if (reqput["title"] == "" or reqput["description"] == ""  or reqput["start_date"] == "" or reqput["end_date"] == "" or 
            reqput["title"] == None or reqput["description"] == None  or reqput["start_date"] == None or reqput["end_date"] == None):
            
            return abort(400, message="fill all fields")
        event = EventSchema().load(request.get_json())
        try:
            event_put = Event.query.filter_by(id=id).first()
            if not event_put:
                raise NoResultFound()

            event_put.title = event.title
            event_put.description = event.description
            event_put.start_date = event.start_date
            event_put.end_date = event.end_date
            db.session.commit()
            return EventSchema().dump(event_put), 201

        except NoResultFound:
            abort(404, message="event not found")








from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from api_Calendar.database import db
from api_Calendar.models.event import Event
from api_Calendar.schemas.EventSchema import EventSchema
"""
PLAYERS_ENDPOINT = "/api/players"
logger = logging.getLogger(__name__)"""

class EventResource (Resource) :
    def get (self, id=None):
        if not id:
            description = request.args.get("description")
            logger.info(
                f"Retrieving all evenst, optionally filtered by position={description}"
            )
            return self._get_all_events(description), 200

        logger.info(f"Retrieving event by id {id}")
        try:
            return self._get_event_by_id(id), 200
        except NoResultFound:
            abort(404, message="event not found")

    def _get_event_by_id(self, event_id):
        event = Event.query.filter_by(event_id=event_id).first()
        event_json = EventSchema().dump(event)

        if not event_json:
            raise NoResultFound()

        logger.info(f"Event retrieved from database {event_json}")
        return event_json

"""
    def _get_all_events(self, position):
        if position:
            players = Player.query.filter_by(position=position).all()
        else:
            players = Player.query.all()

        players_json = [PlayerSchema().dump(player) for player in players]

        logger.info("Players successfully retrieved.")
        return players_json"""

    def post(self):
       
        event = EventSchema().load(request.get_json())

        try:
            db.session.add(event)
            db.session.commit()
        except IntegrityError as e:
            logger.warning(
                f"Integrity Error, this event is already in the database. Error: {e}"
            )

            abort(500, message="Unexpected Error!")
        else:
            return event.event_id, 201






from marshmallow import Schema, fields, post_load
from api_Calendar.models.event import Event

class EventSchema(Schema):
 title= fields.String(allow_none=False)
 description= fields.String(allow_none=False)
 events_id= fields.Integer()
 created_date_start=
 created_date_end=

 @post_load
 def make_event (self, data, **kwargs):
    return Event(**data)

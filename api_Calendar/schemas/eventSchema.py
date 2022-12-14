from marshmallow import Schema, fields, post_load
from api_Calendar.models.events import Event

#create event and validate data type#
class EventSchema(Schema):
   title= fields.String(allow_none=False)
   description= fields.String(allow_none=False)
   id= fields.Integer()
   start_date= fields.DateTime()
   end_date= fields.DateTime()

   @post_load
   def make_event (self, data, **kwargs):
      return Event(**data)

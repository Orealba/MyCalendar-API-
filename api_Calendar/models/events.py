from api_Calendar.database import db
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


class Event(db.Model)
__tablename__="events"
events_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
title = db.Column(db.String(), nullable=False)
description= db.Column(db.String(), nullable=False)
created_date_start = Column(DateTime, default=datetime.datetime.utcnow)
created_date_end = Column(DateTime, default=datetime.datetime.utcnow)

from peewee import CharField, ForeignKeyField, IntegerField, Model, DateTimeField
from datetime import datetime
from .base import BaseModel
from .match import Match


class Meeting(BaseModel):
    match = ForeignKeyField(Match, backref='meetings')

    class Meta:
        db_table = "meeting"

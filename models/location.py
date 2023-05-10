from peewee import CharField
from datetime import datetime
from .base import BaseModel


class Location(BaseModel):
    city = CharField(unique=True)

    class Meta:
        db_table = "location"

from peewee import CharField, ForeignKeyField, IntegerField, Model, DateTimeField
from datetime import datetime
from .user import User
from .location import Location


class Student(User):
    telegram_id = IntegerField(unique=True)
    location = ForeignKeyField(Location, backref="students")
    max_meetings = IntegerField()
    last_matched_time = DateTimeField(null=True)

    class Meta:
        db_table = "student"

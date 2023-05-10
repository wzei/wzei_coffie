from peewee import CharField, ForeignKeyField, IntegerField, Model, DateTimeField
from datetime import datetime
from .base import BaseModel
from .student import Student


class Match(BaseModel):
    student1 = ForeignKeyField(Student, backref='matches1')
    student2 = ForeignKeyField(Student, backref='matches2')

    class Meta:
        db_table = "match"


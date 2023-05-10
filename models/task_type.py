from peewee import CharField, ForeignKeyField, IntegerField, Model, DateTimeField
from datetime import datetime
from .base import BaseModel


class TaskType(BaseModel):
    name = CharField()

    class Meta:
        db_table = "task_type"

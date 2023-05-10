from peewee import CharField
from datetime import datetime
from .base import BaseModel


class DesignPattern(BaseModel):
    name = CharField()

    class Meta:
        db_table = "design_pattern"

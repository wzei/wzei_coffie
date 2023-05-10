from peewee import CharField, ForeignKeyField, IntegerField, Model, DateTimeField
from datetime import datetime
from .base import BaseModel
from .task_type import TaskType
from .design_pattern import DesignPattern


class TaskEntity(BaseModel):
    description = CharField()
    design_pattern = ForeignKeyField(DesignPattern, backref='tasks')
    task_type = ForeignKeyField(TaskType, backref='tasks')
    right_answer = CharField()

    class Meta:
        db_table = "task"

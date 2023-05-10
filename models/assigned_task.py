from peewee import CharField, ForeignKeyField, IntegerField, Model, DateTimeField
from datetime import datetime
from .base import BaseModel
from .task_entity import TaskEntity
from .student import Student
from .meeting import Meeting


class AssignedTask(BaseModel):
    task = ForeignKeyField(TaskEntity, backref='assigned_tasks')
    student = ForeignKeyField(Student, backref='assigned_tasks')
    meeting = ForeignKeyField(Meeting, backref='assigned_tasks')

    class Meta:
        db_table = "assigned_task"

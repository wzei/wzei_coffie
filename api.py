from flask import Flask, request, jsonify
from models import TaskEntity, DesignPattern, TaskType, Student, Location, Match, Meeting, AssignedTask
from peewee import SqliteDatabase, PostgresqlDatabase
# from data import config
from pathlib import Path

DIR = Path(__file__).absolute()


app = Flask(__name__)
database = SqliteDatabase(f'{DIR}/data/database.sqlite3')


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskEntity.select()
    return jsonify([task.serialize() for task in tasks])


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_type = TaskType.get(TaskType.name == data['task_type'])
    design_pattern = DesignPattern.get(DesignPattern.name == data['design_pattern'])
    task = TaskEntity.create(description=data['description'], task_type=task_type, design_pattern=design_pattern,
                             right_answer=data['right_answer'])
    return jsonify(task.serialize())


@app.route('/students', methods=['GET'])
def get_students():
    students = Student.select()
    return jsonify([student.serialize() for student in students])


@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    location = Location.get(Location.city == data['location'])
    student = Student.create(name=data['name'], telegram_id=data['telegram_id'], location=location,
                             max_meetings=data['max_meetings'])
    return jsonify(student.serialize())


@app.route('/assigned_tasks', methods=['POST'])
def assign_task():
    data = request.json
    task = TaskEntity.get(TaskEntity.id == data['task_id'])
    student = Student.get(Student.telegram_id == data['telegram_id'])
    meeting = Meeting.get(Meeting.id == data['meeting_id'])
    assigned_task = AssignedTask.create(task=task, student=student, meeting=meeting)
    return jsonify(assigned_task.serialize())


if __name__ == '__main__':
    app.run(debug=True)

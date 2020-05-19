from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import random

app = Flask(__name__)
api = Api(app, version="1.0", title="My first CRUD REST API",
          description="TODO list and CRUD options for it")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://nikonikoni:niko1324@localhost:5432/Sberbank"

db = SQLAlchemy(app)

todo = api.model("New TODO: ", {
    "id": fields.Integer(readonly=True, description="The task unique key", min=1),
    "task": fields.String(required=True, description="What's you need to do")})

namespace = api.namespace("todo_list", description="options for todo list")

class Task(db.Model):
    __tablename__ = "Todos"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), unique=True)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return "<task %r>" % self.task

db.create_all()
class TodoManager(object):
    def get_by_id(self, id):
        return Task.query.get_or_404(id)

    def get_all(self):
        all_tasks = Task.query.all()
        return all_tasks

    def delete(self, id):
        todo = Task.query.get(id)
        db.session.delete(todo)
        db.session.commit()
        #return self.get_all()

    def update(self, id, data):
        todo = Task.query.get(id)
        task = request.json["task"]
        todo.task = task
        db.session.commit()
        return todo

    def create(self, data):
        new_todo = Task(data["task"])
        db.session.add(new_todo)
        db.session.commit()
        return new_todo

tm = TodoManager()

@namespace.route("/")
class TodoList(Resource):
    @namespace.doc("ALL TODO LIST")
    @namespace.marshal_list_with(todo)
    @api.expect()
    def get(self):
        return tm.get_all()

    @namespace.doc("ADD SOME TODO")
    @namespace.expect(todo)
    @namespace.marshal_with(todo, code=201)
    def post(self):
        return tm.create(api.payload), 201


@namespace.route("/<int:id>")
@namespace.response(404, "Todo not found")
@namespace.param("id", "Unique todo key")
class Todo(Resource):
    @namespace.doc("GET TODO BY UNIQUE TODO'S KEY")
    @namespace.marshal_with(todo)
    def get(self, id):
        return tm.get_by_id(id)

    @namespace.doc("DELETE TODO BY UNIQUE TODO'S KEY")
    @namespace.response(204, "todo deleted")
    def delete(self, id):
        return tm.delete(id), 204

    @namespace.expect(todo)
    @namespace.marshal_with(todo)
    def put(self, id):
        return tm.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)

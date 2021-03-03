from flask import Blueprint, render_template,redirect, url_for, request
from projects.extensions import mongo
from bson.objectid import ObjectId
main = Blueprint('main', __name__)


@main.route('/')
def index():
    todos_collection = mongo.db.todo
    todos = todos_collection.find()
    return render_template('index.html', todos=todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todo
    todo = request.form.get('todo')
    todos_collection.insert_one({'text': todo, 'complete': False})
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todos_collection = mongo.db.todo
    todo_item = todos_collection.find_one({'_id': ObjectId(oid)})
    todo_item['complete'] = True
    todos_collection.save(todo_item)
    return redirect(url_for('main.index'))

@main.route('/delete_completed')
def delete_completed():
    todos_collection = mongo.db.todo
    todos_collection.delete_many({'complete': True})
    return redirect(url_for('main.index'))

@main.route('/delete_all')
def delete_all():
    todo_collection = mongo.db.todo
    todo_collection.delete_many({})
    return redirect(url_for('main.index'))
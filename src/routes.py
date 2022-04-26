from flask import jsonify, request
from src import app
from src import db
from src.users.users import User
from src.notes.notes import Notes


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        newUser = User(name= data['name'], email= data['email'], password= data['password'] )
        db.session.add(newUser)
        db.session.commit()
        return data
    else:
        users = User.query.all()
        print(users)
        return jsonify([user.serialize for user in users])


@app.route('/users/<user_id>')
def user(user_id):
    user = User.query.get(user_id)
    print(user)
    return user.serialize


@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.get(data["owner_id"])
        newNote = Notes(title= data['title'], note_text= data['note_text'], owner= user)
        db.session.add(newNote)
        db.session.commit()
        return data
    else:
        notes = Notes.query.all()
        print(notes)
        return jsonify([note.serialize for note in notes])


@app.route('/notes/<note_id>')
def note(note_id):
    note = Notes.query.get(note_id)
    print(note)
    return note.serialize

@app.route('/notes/<note_id>')
def note(note_id):
    note = Notes.query.get(note_id)
    print(note)
    return note.serialize

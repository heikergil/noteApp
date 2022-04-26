from src import app
from src import db
from src.users.users import User
from src.notes.notes import Notes


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Notes': Notes}

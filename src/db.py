from flask_sqlalchemy import SQLAlchemy
from decouple import config
from datetime import datetime

from flask import Flask

app = Flask(__name__)


def get_env_variable(name):
    try:
        return config(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup


# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")


DB_URL = 'postgresql+psycopg2://postgres:root@localhost:5432/flask_db'

# DB_URL = 'sqlite:///flask_notes.db'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# silence the deprecation warning

db = SQLAlchemy(app)


# CREATE TABLE `users` (
#   `id` UUID,
#   `name` VARCHAR (50),
#   `email` VARCHAR (50),
#   `password` VARCHAR (50),
#   `tokens` VARCHAR (300),
#   `timestamp` UUID,
#   `role_id` VARCHAR (50),
#   PRIMARY KEY (`id`),
#   FOREIGN KEY (`role_id`) REFERENCES `roles`(`id`)
# );

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username


# CREATE TABLE "notes" (
#   "id" UUID,
#   "note_text" VARCHAR (300),
#   "timestamp" UUID,
#   "owner" UUID,
#   "title" VARCHAR (50),
#   "category_id" UUID,
#   PRIMARY KEY ("id"),
#   CONSTRAINT "FK_notes.category_id"
#     FOREIGN KEY ("category_id")
#       REFERENCES "category"("id"),
#   CONSTRAINT "FK_notes.timestamp"
#     FOREIGN KEY ("timestamp")
#       REFERENCES "timestamps"("id")
# );

class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    note_text = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    category = db.relationship('Category',
                            backref=db.backref('notes', lazy=True))

    def __repr__(self):
        return '<Title %r>' % self.title


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name

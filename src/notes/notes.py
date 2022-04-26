from src import db
from datetime import datetime


class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, index=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    note_text = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return self.title

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'title': self.title,
            'timestamp': self.timestamp,
            'note_text': self.note_text,
            'user_id': self.user_id
        }

from src import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    email = db.Column(db.String(80), unique=True, index=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    notes = db.relationship('Notes', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

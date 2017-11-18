from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    first_name = db.Column(db.String(128), unique=True, nullable=False)
    last_name = db.Column(db.String(128), unique=True, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
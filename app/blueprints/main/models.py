from app import db
from datetime import datetime as dt
from app import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    comics_appeared_in = db.Column(db.Integer)
    super_power = db.Column(db.String(250))
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        from app.blueprints.auth.models import User

        data = {
            'id': self.id,
            'body': self.body,
            'date_created': self.date_created,
            'user': User.query.get(self.user_id).to_dict()
        }
        return data

    def from_dict(self, data):
        for field in ['body', 'user_id']:
            if field in data:
                setattr(self, field, data[field])
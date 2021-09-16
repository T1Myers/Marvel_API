from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(250))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def create_password_hash(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, current_password):
        return check_password_hash(self.password, current_password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
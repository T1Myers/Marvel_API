from app import db
from datetime import datetime as dt
from app import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



# HASHING AND SALTING

# lucas-hash
# derek-hash

# HASHING
# password = abc123
# translation => er7p98789arhuo8bozufjn2

# SALTING
# real password for password 1 = abc123
# original = er7p98789arhuo8bozufjn2
# salt = 2q480we89b801dfuuoijsriodfuo

# real password for password 2 = abc123
# original = er7p98789arhuo8bozufjn2
# salt = 84yar8h90fd9n80uO2YAH09

# REAL_PASSWORD = ABC123
# salt = 84yar8h90fd9n80uO2YAH09
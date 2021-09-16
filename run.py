from app.blueprints.auth.models import User
from app import db, create_app
from app.models import Post

app = create_app()

@app.shell_context_processor
def make_context():
    return {
        'Post': Post,
        'User': User,
        'db': db
    }
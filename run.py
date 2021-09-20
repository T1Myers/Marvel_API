from app.blueprints.auth.models import User
from app import db, create_app
from app.blueprints.main.models import Character

app = create_app()

@app.shell_context_processor
def make_context():
    return {
        'Character': Character,
        'User': User,
        'db': db
    }
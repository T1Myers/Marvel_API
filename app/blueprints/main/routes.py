from flask.helpers import url_for
from app import db
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import Character
from .import bp as app

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        p = Character(
                name=request.form.get('name'),
                user_id=1
            )
        db.session.add(p)
        db.session.commit()
        flash('Post created successfully', 'success')
        return redirect(url_for('main.home'))
    context = {
        'character': Character.query.order_by(Character.date_created.desc()).all()
    }
    return render_template('home.html', body='This is the first post', first_name='Derek', last_name='Lang', date_posted=9)
    return render_template('home.html', **context)
    # **context

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


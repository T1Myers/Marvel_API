from app.blueprints.auth.models import User
from .import bp as app
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # look for the user in our database
        user = User.query.filter_by(email=email).first()
        # if the email and/or password don't match,
        if user is None or not user.check_password(password):
            # show an error messages
            flash('You typed in either an incorrect email or password', 'danger')
            # redirect to the login page
            return redirect(url_for('auth.login'))
        # otherwise
        # log the user in
        login_user(user)
        flash('You have logged in successfully!', 'info')
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out successfully', 'primary')
    return redirect(url_for('home'))
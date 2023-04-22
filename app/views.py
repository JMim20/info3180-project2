"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, jsonify, request, send_file, send_from_directory, url_for
import os
from .models import Post, Like,Follow, User
from werkzeug.utils import secure_filename
from .forms import RegisterForm, LoginForm
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required




###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


#Register route - Accepts user information and saves it to the database
@app.route("/api/v1/register", methods=['POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            firstname = form.firstname.data
            lastname = form.lastname.data
            email= form.email.data
            location = form.location.data
            biography = form.biography.data
            profile_photo = form.profile_photo.data
            
            filename= secure_filename(profile_photo.filename)
            profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            newUser= User(username,password, firstname, lastname, email, location, biography, filename)
            db.session.add(newUser)
            db.session.commit()

            return jsonify({
                "message": "User Successfully registered",
                "username": newUser.username,
                "password": newUser.password,
                "firstname": newUser.firstname,
                "lastname": newUser.lastname,
                "email": newUser.email,
                "location": newUser.location,
                "biography": newUser.biography,
                "profile_photo": newUser.profile_photo,
                "joined_on": newUser.joined_on
            })

        else:
            return jsonify({'errors': form_errors(form)})
        
#Login Route- Accepts login credentials as username and password

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = db.session.execute(db.select(User).filter_by(username=username)).scalar()
    
        if user is not None and check_password_hash(user.password, password):
            # remember_me = False

            # if 'remember_me' in request.form:
            #     remember_me = True

            login_user(user)
            return jsonify({
                "message": "logged in Successfully!",
                "username": username,
                "password": password
            })
    else:
        return jsonify({'errors': form_errors(form)})
    
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(User).filter_by(id=id)).scalar()

""" #Logout a user
@app.route("/api/v1/auth/logout", method =['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({
                "message": "You have been logged out!",
            }) """

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
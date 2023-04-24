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
from .forms import RegisterForm, LoginForm, NewPostForm
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
import datetime
import jwt
from functools import wraps


#Decorator functions for JWT Authentication
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None)
    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
         payload = jwt.decode(token, app.config['SECRET_KEY'])

    except jwt.ExpiredSignature:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    current_user = user = payload
    return f(*args, **kwargs)

  return decorated



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
    
""" @login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(User).filter_by(id=id)).scalar()
 """
#Logout a user
""" @app.route("/api/v1/auth/logout", method =['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({
                "message": "You have been logged out!",
            })
 """

@app.route("/api/auth/logout", methods=["GET"])
@login_required
def logout():
    logout_user()

    #Flash message for successful logout
    response = "You were logged out successfully."
    return jsonify(message=response)


@app.route('/api/users/<user_id>/posts', methods = ['GET', 'POST'])
def post (user_id):
    form = NewPostForm()
    if request.method == "POST" and form.validate_on_submit():
        photo = form.photo.data
        caption = form.caption.data
        date = datetime.datetime.now()
        date = date.strftime("%d %b %Y")

        file = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], file))

        path = url_for('static', filename= "images/photos/"+file)

        post = Post(user_id=int(user_id), photo=path, caption=caption, created_on=date)
        db.session.add(post)
        db.session.commit()
        
        return jsonify({"Post" : "yes"})

    if request.method == "GET":
        auth = request.headers.get('Authorization', None)
        parts = auth.split()
        token = parts[1]
        myId = (jwt.decode(token, 'app.config[SECRET_KEY]')['user_id'])
        
        user = User.query.filter_by(id=int(user_id)).first()
        posts = Post.query.filter_by(user_id=int(user_id)).count()
        follows = Follow.query.filter_by(user_id=int(user_id)).count()
        followers = Follow.query.filter_by(user_id=int(user_id))
        followersList = []
        for follower in followers:
            followersList.append(follower.user_id)

        following = myId in followersList
        d = {}
        d['uid'] = user.id
        d['pphoto'] = user.profile_photo
        d['fname'] = user.firstname
        d['lname'] = user.lastname
        d['location'] = user.location
        d['bio'] = user.biography
        d['date'] = user.joined_on
        d['posts'] = posts
        d['follows'] = follows
        d['following'] = following

        return jsonify(d=d)
    return jsonify({"Post" : "Not Valid"})


""" Create a Follow relationship between the current user and the target user"""

@app.route('/api/users/<user_id>/follow', methods = ['POST'])
def follow (user_id):
    if request.method == "POST":
        auth = request.headers.get('Authorization', None)
        parts = auth.split()
        if parts[0].lower() == 'bearer':
            token = parts[1]
            followID = jwt.decode(token, 'app.config[SECRET_KEY]')

            follow = Follow(user_id=int(user_id),follower_id=int(followID['user_Id']))
            db.session.add(follow)
            db.session.commit()
            user = User.query.filter_by(id=int(user_id)).first()
            posts = Post.query.filter_by(user_id=int(user_id)).count()
            follows = Follow.query.filter_by(user_id=int(user_id)).count()
            d = {}
            d['uid'] = user.id
            d['pphoto'] = user.profile_photo
            d['fname'] = user.firstname
            d['lname'] = user.lastname
            d['location'] = user.location
            d['bio'] = user.biography
            d['date'] = user.joined_on
            d['posts'] = posts
            d['follows'] = follows
            return jsonify(d=d)
    return jsonify({"Follow" : "failed"})


"""Return all posts for all users"""
@app.route('/api/posts', methods = ['GET'])
@requires_auth
def all_post ():
    posts = db.session.query(Post).all()
    
    auth = request.headers.get('Authorization', None)
    parts = auth.split()
    token = parts[1]
    myId = (jwt.decode(token, 'app.config[SECRET_KEY]')['user_Id'])
    
    list2 = []
    for post in posts:
        d = {}
        uid = post.user_id
        user = User.query.filter_by(id=int(id)).first()
        d['uid'] = uid
        d['pphoto'] = user.profile_photo
        d['user'] = user.username
        d['pid'] = post.id
        d['photo'] = post.photo
        d['caption'] = post.caption
        d['date'] = post.created_on
        likes = Like.query.filter_by(post_id=int(post.id)).count()
        likers = Like.query.filter_by(post_id=int(post.id))
        likersList =[]
        for like in likers:
            likersList.append(like.user_id)
        like = myId in likersList
        d['likes'] = likes
        d['like'] = like
        list2.append(d)

    data = dict(list(enumerate(list2)))
    return jsonify(data=data)

"""Set a like on the current Post by the logged in User"""

@app.route('/api/posts/<post_id>/like', methods = ['POST'])
def like (post_id):
    if request.method == "POST":
        auth = request.headers.get('Authorization', None)
        parts = auth.split()
        if parts[0].lower() == 'bearer':
            token = parts[1]
            liker = jwt.decode(token, 'app.config[SECRET_KEY]')
            
            like = Like(user_id=int(liker['user_Id']),post_id=int(post_id))
            db.session.add(like)
            db.session.commit()
            return all_post()
    return jsonify({"Follow" : "failed"})


"""Route for User to View Profile"""
@app.route('/api/profile', methods = ['GET'])
@requires_auth
def profile():
    if request.method == "GET":
        auth = request.headers.get('Authorization', None)
        parts = auth.split()
        token = parts[1]
        uid = (jwt.decode(token, 'app.config[SECRET_KEY]')['user_Id'])
        user = User.query.filter_by(id=int(uid)).first()
        followers = Follow.query.filter_by(user_id=int(uid)).count()
        following = Follow.query.filter_by(follower_id=int(uid)).count()
        d = {}
        d['pphoto'] = user.profile_photo
        d['user'] = user.username
        d['fname'] = user.firstname
        d['lname'] = user.lastname
        d['location'] = user.location
        d['email'] = user.email
        d['bio'] = user.biography
        d['date'] = user.joined_on
        d['followers'] = followers
        d['following'] = following

        return jsonify(d=d)
    return jsonify({"Profile" : "no"})
    

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

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
# Add any model classes for Flask-SQLAlchemy here

from . import db
from datetime import datetime
from flask import url_for
from werkzeug.security import generate_password_hash

class Post(db.Model):
    
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(200))
    photo=db.Column(db.String(250))
    user_id = db.Column(db.Integer, nullable=False)
    created_on=db.Column(db.DateTime(), nullable=False)


    def __init__(self, caption, photo, user_id):
        self.caption = caption
        self. photo =  photo
        self.user_id = user_id
        self.created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def serialize(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "photo": url_for('getImage', filename=self.photo),
            "user_id": self.user_id,
            "created_on": self.created_on
        }  


    def __repr__(self):
        return '<Post %r>' % (self.user_id)
    


class Like(db.Model):
    
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    

    def __init__(self,  post_id, user_id):
        self.post_id =  post_id
        self.user_id = user_id


    def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "user_id": self.user_id,
        }  


    def __repr__(self):
        return '<Like %r>' % (self.post_id)
    


class Follow(db.Model):
    
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    

    def __init__(self, follower_id, user_id):
        self.follower_id = follower_id
        self.user_id = user_id


    def serialize(self):
        return {
            "id": self.id,
            "follower_id": self.follower_id,
            "user_id": self.user_id,
        }  


    def __repr__(self):
        return '<Follower %r>' % (self.follower_id)



class User(db.Model):

    __tablename__ = 'users_'

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(128), unique = True)
    password = db.Column(db.String(128), nullable = False)
    firstname=db.Column(db.String(250), nullable = False)
    lastname=db.Column(db.String(250), nullable = False)
    email=db.Column(db.String(200), nullable = False)
    location=db.Column(db.String(200), nullable = False)
    biography=db.Column(db.String(300), nullable = False)
    profile_photo=db.Column(db.Text(),nullable = False)
    joined_on = db.Column(db.DateTime(), nullable = False)


    def __init__(self, username, password, firstname, lastname, email, location, biography, profile_photo):
        self.username = username
        self.password = generate_password_hash(password)
        self.firstname =firstname
        self.lastname =lastname
        self.email =email
        self.location =location
        self.biography =biography
        self.profile_photo =profile_photo
        self.joined_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "location": self.location,
            "biography": self.biography,
            "profile_photo":  self.profile_photo,
            "joined_on": self.joined_on,
        }
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  
        except NameError:
            return str(self.id) 

    def __repr__(self):
        return "<User %r>" % (self.username)
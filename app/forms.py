# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    location= StringField('Location', validators=[InputRequired()])
    biography = StringField('Biography', validators=[InputRequired()])
    profile_photo= FileField('Photo', validators=[FileAllowed(['jpg','JPG','png','PNG'],'JPG OR PNG- IMAGES FILES ONLY!')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class NewPostForm(FlaskForm):
    photo = FileField('photo', validators=[FileAllowed(['jpg','JPG','png','PNG'],'JPG OR PNG- IMAGES FILES ONLY!')])
    caption = TextAreaField('Caption', validators=[InputRequired()])

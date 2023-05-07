from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager

UPLOAD_FOLDER = './app/Uploads'
SECRET_KEY= 'Som3$ec5etK*y'

app = Flask(__name__)
app.config.from_object(Config)

csrf = CSRFProtect(app)

app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:Postgres@localhost/Project2'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views
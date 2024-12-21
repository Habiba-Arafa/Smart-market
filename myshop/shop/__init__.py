from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager

# Initialize app
app = Flask(__name__)

# Configurations
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = 'hfouewhfoiwefoquw'
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"

# Import routes (after initializing app and extensions)
from shop.admin import routes
from shop.products import routes
from shop.customers import routes







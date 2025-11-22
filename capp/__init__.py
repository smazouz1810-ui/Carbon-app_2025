from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os 
from flask_login import LoginManager

application = Flask(__name__)
application.secret_key = os.environ.get("SECRET_KEY", "une_cle_ultra_secrete_a_changer")

# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
# application.config['SQLALCHEMY_BINDS'] = {'transport': 'sqlite:///transport.db'}
# application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


from capp.home.routes import home
from capp.calculator.routes import calculator
from capp.foryou.routes import foryou
from capp.aboutus.routes import aboutus
from capp.users.routes import users



application.register_blueprint(home)
application.register_blueprint(calculator)
application.register_blueprint(foryou)
application.register_blueprint(aboutus)
application.register_blueprint(users)

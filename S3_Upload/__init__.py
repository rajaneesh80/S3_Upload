import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
#from S3_Upload.users.forms import Update_image
from config import Config


#app = Flask(__name__)

app = Flask(__name__, instance_relative_config=True)

# CONFIG

app.config.from_object(Config)

########################################################################################

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     from S3_Upload.users import bp as users_bp
#     app.register_blueprint(users_bp)
#     return app

#### BLUEPRINT CONFIGS #######

from S3_Upload.users.routes import users

# Register the apps

app.register_blueprint(users)

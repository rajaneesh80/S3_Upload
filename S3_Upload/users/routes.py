import os
from flask import Flask, render_template, request, redirect, Blueprint
from werkzeug.utils import secure_filename
from S3_Upload.users.forms import Update_image


########################################################################################

from S3_Upload.tools import upload_file_to_s3




# ROUTES
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



users = Blueprint('users', __name__)


@users.route('/', methods=['GET','POST'])
def upload_file():
    form = Update_image()

    return render_template('index.html', form=form)
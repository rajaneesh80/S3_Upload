from flask import Flask, render_template, request, redirect, Blueprint
from werkzeug.utils import secure_filename
from S3_Upload.users.forms import Update_image



users = Blueprint('users', __name__)


@users.route('/', methods=['GET','POST'])
def upload_file():
    form = Update_image()

    return render_template('index.html', form=form)
import os
from S3_Upload import app
from flask import Flask, render_template, request, redirect, Blueprint
from werkzeug.utils import secure_filename
#from S3_Upload.users.forms import Update_image
from S3_Upload.tools import upload_file_to_s3, list_files_in_s3, delete_file_from_s3


########################################################################################

from S3_Upload.tools import upload_file_to_s3

ALLOWED_EXTENSIONS = app.config["ALLOWED_EXTENSIONS"]

###############################################################

# ROUTES

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

##################################################################

users = Blueprint('users', __name__)

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@users.route('/', methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		file    = request.files["user_file"]

		if file.filename and allowed_file(file.filename):
			file.filename = secure_filename(file.filename)
			output   	  = upload_file_to_s3(file, app.config["S3_BUCKET"])
			return str(output)
	else:
		return render_template('index.html')




#form = Update_image()
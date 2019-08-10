# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed


# class Update_image(FlaskForm):
# 	picture = FileField('Update_Iamge', validators=[FileAllowed(['jpg', 'png'])])
# 	submit = SubmitField('Summit')


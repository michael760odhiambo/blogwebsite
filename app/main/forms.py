from wtforms import SubmitField,StringField,PasswordField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from flask_wtf import FlaskForm

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself', validators=[Required()])
    submit = SubmitField('submit','success')
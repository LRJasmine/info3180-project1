from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, validators
from wtforms.validators import DataRequired, Email, Length


class AddProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender =  SelectField('Gender', choices=[('default','Select Gender'),('male','Male'),('female','Female')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired(), Length(max=250)])
    profilephoto = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
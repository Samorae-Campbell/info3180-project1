from flask.ext.wtf import Form

from wtforms.fields import TextField, SelectField

# other fields include PasswordField

from wtforms.validators import Required, Email

#from flask.ext.uploads import UploadSet, IMAGES
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired

class EmailPasswordForm(Form):

  fname = TextField('First_name', validators=[Required()])
  
  lname = TextField('Last_name', validators=[Required()])

  email = TextField('Email', validators=[Required(), Email()])
  
  age = TextField('Age', validators=[Required()])
  
  sex = SelectField('Sex', choices=[('Male', 'Male'),('Female', 'Female')], validators=[Required()])
  
  image = FileField('Image', validators=[
        FileRequired()
    ])
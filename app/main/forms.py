from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Add your Comments here.',validators = [Required()])
    submit = SubmitField('Submit')


class CategoriesForm(FlaskForm):
	name = TextAreaField('ADD YOUR CATEGORIES HERE')
	submit = SubmitField('SUBMIT')


class PitchForm(FlaskForm):
   
  pitch = TextAreaField('Add your Pitches here.',validators = [Required()])
  submit = SubmitField('Submit')


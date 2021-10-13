from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Regexp


class UserInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[Regexp(r'\d{3}-\d{3}-\d{4}')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')



from app import app, db
from flask import render_template
from app.forms import UserInfoForm
from app.models import User


@app.route('/')
def index():
    name = "Jerome's Phone Book"
    title = 'Coding Temple Flask'
    return render_template('index.html', name_of_user=name, title=title)



@app.route('/register', methods=["GET", 'POST'])
def register():
    register_form = UserInfoForm()
    if register_form.validate_on_submit():
        print('Hello this form has been submitted correctly')
        username = register_form.username.data
        phone = register_form.phone.data
        password = register_form.password.data
        print(username, phone, password)

        new_user = User(username, phone, password)

        db.session.add(new_user)
        db.session.commit()
        
    return render_template('register.html', form=register_form)


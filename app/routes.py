from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import UserInfoForm, LoginForm, NumberForm
from app.models import User, Phone
from flask_login import login_user, logout_user, current_user, login_required


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

        return redirect(url_for('index'))
    return render_template('register.html', form=register_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab data from form
        username = form.username.data
        password = form.password.data

        # Query our User table for a user with username
        user = User.query.filter_by(username=username).first()

        # Check if the user is None or if password is incorrect
        if user is None or not user.check_password(password):
            flash('Your username or password is incorrect', 'danger')
            return redirect(url_for('login'))
        print(user)
        login_user(user)

        flash(f'Welcome {user.username}. You have succesfully logged in.', 'success')

        return redirect(url_for('my_post'))
        

    return render_template('login.html', login_form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/my_post')
@login_required
def my_post():
    numbers = Phone.query.all()
    return render_template('my_post.html', numbers=numbers)

@app.route('/each_pbook')
@login_required
def each_number():
    numbers = current_user.phone
    return render_template('each_pbook.html', numbers=numbers)

@app.route('/phone_number', methods=['GET', 'POST'])
@login_required
def createnumber():
    form = NumberForm()
    if form.validate_on_submit():
        print('Hello')
        name = form.name.data
        phone = form.phone.data
        new_post = Phone(name, phone, current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('my_post'))
    return render_template('phone_number.html', form=form)


from app import db, login_manager
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)


    def __init__(self, username, phone, password):
        self.username=username
        self.phone = phone
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200))
    phone = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, phone, user_id):
        self.name = name
        self.phone = phone
        self.user_id = user_id
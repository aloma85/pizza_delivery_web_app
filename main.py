from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, IntegerField, DecimalField, \
    SelectMultipleField


basdir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
login_manager = LoginManager()

app.config["SECRET_KEY"] = "Youwillneverguess"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basdir, "pizza.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)
login_manager.init_app(app)
login_manager.login_view = "login"

admin = Admin(app)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(50000), nullable=False)
    toping = db.Column(db.String(50000))
    photo = db.Column(db.String(255), nullable=False)
    order_items = db.relationship("Order_item", backref="products", lazy=True)



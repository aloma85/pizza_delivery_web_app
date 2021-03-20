from flask import Flask, render_template,request , redirect , flash , url_for , session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager,UserMixin,login_required,current_user,login_user,logout_user


basdir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
login_manager = LoginManager()





app.config["SECRET_KEY"]="Youwillneverguess"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basdir , "pizza.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
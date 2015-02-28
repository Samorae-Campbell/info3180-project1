from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://kwuoxfieyolizi:KkHVx445S2fFDxZ9KZnW87nfKh@ec2-23-23-180-133.compute-1.amazonaws.com:5432/dabrcfl2c5jikk'

db = SQLAlchemy(app)

from app import views, models
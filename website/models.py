from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func





class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    


# Define the Job model
class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    Company = db.Column(db.String(255))
    Role = db.Column(db.String(255))
    Location = db.Column(db.String(255))
    Date = db.Column(db.String(255))
    Application = db.Column(db.Integer)
    Link = db.Column(db.String(255))




class Rating(db.Model):
    __tablename__ = 'ratings'
    RID = db.Column(db.Integer, primary_key=True)
    UID = db.Column(db.Integer)
    CID = db.Column(db.Integer)
    Mscore = db.Column(db.Float)
    CL = db.Column(db.TEXT )
    UID = db.Column(db.Integer, db.ForeignKey('user.id'))
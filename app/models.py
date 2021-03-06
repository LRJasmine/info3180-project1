import datetime
from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    email = db.Column(db.String(120), unique=True) 
    location = db.Column(db.String(120))
    biography = db.Column(db.String(250))
    profile_picture = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    
    def __init__(self, first_name, last_name, gender, email, location, biography, profile_picture, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_picture = profile_picture
        self.date_joined = date_joined


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)

app.config['SECRET_KEY'] = "b'\xe6\xa5H\x92\x9bQ\x87\x01;{\xbe\xdcd2\xc6\xad\x0b\r\x83T\x10\x8e\xeb<'"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
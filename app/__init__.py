from flask import Flask

app = Flask(__name__)
from app import views

app.config['SECRET_KEY'] = "b'\xe6\xa5H\x92\x9bQ\x87\x01;{\xbe\xdcd2\xc6\xad\x0b\r\x83T\x10\x8e\xeb<'"


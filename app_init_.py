from database.createSQL import Book, Song, Author, PublishURL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__,instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./onpuscores.db'

db = SQLAlchemy(app)

per_page = 30

import rootes

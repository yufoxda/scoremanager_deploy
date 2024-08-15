


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__,instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onpuscores.db'


db = SQLAlchemy(app)

per_page = 30

import rootes

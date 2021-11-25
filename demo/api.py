from flask import Flask, jsonify, request
from flask_sqlalchemy import abort
from model import *
from dotenv import load_dotenv
import os

# Getting credentials
load_dotenv()
user_name = os.environ.get('DATABASE_USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
database = os.environ.get('DATABASE')

# Initializing the application
app = Flask(__name__)

# Connecting to the postgres server
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_name}:{password}@{host}:5432/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connecting the db with the application
db.init_app(app)

# Starting working on routes


if __name__ == '__main__':
    # we set the debug to True so we can see error and which endpoint was hit in the console
    app.run(debug=True)

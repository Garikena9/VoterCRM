from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


application = Flask(__name__)
application.secret_key = 'flask-VoterCRM-Backend-1234'
api = Api(application)  # Flask restful wraps Flask app around it.

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/voter_crm'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(application)
# print(type(db))
# print(db)
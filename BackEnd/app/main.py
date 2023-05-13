from Backend.app import application, db
from Backend.app.APIs.Admin_Auth_API import *
from Backend.app.Models import *
from Backend.app.Authentication.jwtservice import JWTService
from Backend.app.Authentication.middleware import Middleware
from Backend.app.Authentication.hashingservice import HashingService
from flask import request
from werkzeug import exceptions
import uuid

if __name__ == "__main__":
    application.run(debug=True, port=8000)

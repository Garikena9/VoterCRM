from Backend.app import application
from Backend.app.APIs.Admin_Auth_API import Admin_Auth_API_blueprint
from Backend.app.APIs.States_API import States_API_blueprint
from Backend.app.APIs.Districts_API import Districts_API_blueprint
from Backend.app.APIs.AssemblyConstituency_API_blueprint import AssemblyConstituency_API_blueprint
from Backend.app.Models import *
from flask import request


application.register_blueprint(Admin_Auth_API_blueprint)
application.register_blueprint(States_API_blueprint)
application.register_blueprint(Districts_API_blueprint)
application.register_blueprint(AssemblyConstituency_API_blueprint)

if __name__ == "__main__":
    application.run(debug=True, port=8000)

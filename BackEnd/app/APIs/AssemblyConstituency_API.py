# import sys, os
# sys.path.append('c:/Users/darsh/OneDrive/Desktop/VoterCRM_Backend_main/VoterCRM_Backend/BackEnd')

from Backend.app.__init__ import application,db
from Backend.app.Models.AssemblyConstituency import AssemblyConstituency
from Backend.app.Authentication.jwtservice import JWTService
from Backend.app.Authentication.middleware import Middleware
from flask import request, Blueprint

# from app import application, db
# from app.Models.AssemblyConstituency import AssemblyConstituency
# from app import db
# from app.Authentication.jwtservice import JWTService
# from app.Authentication.middleware import Middleware
# from flask import request, Blueprint


jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)

application.before_request(lambda: middleware.auth(request))

AssemblyConstituency_API_blueprint = Blueprint("AssemblyConstituency_API", __name__)

@AssemblyConstituency_API_blueprint.route("/admin/assemblyconstituency", methods=["GET"])
def get_all_constituencies():
    constituency = AssemblyConstituency.query.all()
    if constituency:
        constituency_list = []
        for constituency in constituency:
            constituency_dict = {}
            constituency_dict["Constituency_Id"] = constituency.Constituency_Id
            constituency_dict["Constituency_Name"] = constituency.Constituency_Name
            constituency_dict["Constituency_No"] = constituency.Constituency_No
            constituency_dict["District_Code"] = constituency.District_Code
            constituency_list.append(constituency_dict)
        return {"constituency": constituency_list}
    else:
        return {"message": "No constituency Available"}

@AssemblyConstituency_API_blueprint.route("/admin/add_constituency", methods=["POST"])
def add_constituency():
    body = request.json
    constituency = AssemblyConstituency(body["Constituency_Id"], body["Constituency_Name"], 
                                        body["Constituency_No"],body["District_Code"])
    db.session.add(constituency)
    db.session.commit()
    return {"message": "New constituency added successfully"}

@AssemblyConstituency_API_blueprint.route("/admin/delete_constituency", methods=["DELETE"])
def constituency_delete():
    body = request.json
    constituency = AssemblyConstituency.query.get(body["Constituency_Id"])
    db.session.delete(constituency)
    db.session.commit()

    return "Constituency was successfully deleted"

# Endpoint for updating a guide
@AssemblyConstituency_API_blueprint.route("/admin/update_constituency_name", methods=["PUT"])
def constituesncy_update():
    body = request.json
    constituency = AssemblyConstituency.query.get(body["Constituency_Id"])
    Constituency_Name = request.json['Constituency_Name']
    Constituency_No = request.json['Constituency_No']
    if Constituency_Name:
        constituency.Constituency_Name = Constituency_Name
    if Constituency_No:
        constituency.Constituency_No = Constituency_No
    db.session.commit()
    return "Constituency was successfully updated"
    
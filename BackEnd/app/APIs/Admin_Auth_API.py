from Backend.app import application, db
from Backend.app.Models.Agents import Agents
from Backend.app.Authentication.jwtservice import JWTService
from Backend.app.Authentication.middleware import Middleware
from Backend.app.Authentication.hashingservice import HashingService
from flask import request, Blueprint
from werkzeug import exceptions
import uuid

sign_up_key = "signupkey"
jwt_secret = "secret"

jwt_service = JWTService(jwt_secret)
middleware = Middleware(jwt_service)
hashing_service = HashingService()

application.before_request(lambda: middleware.auth(request))

Admin_Auth_API_blueprint = Blueprint('Admin_Auth_API', __name__)

@Admin_Auth_API_blueprint.route("/api/auth/login", methods=["POST"])
def log_in():
    username, password = request.json["Username"], request.json["Password"]
    admin = Agents.query.filter_by(Username=username).first()
    if admin is None:
        return exceptions.Unauthorized(
            description="Incorrect username/password combination"
        )
    is_password_correct = hashing_service.check_bcrypt(
        password.encode("utf-8"), admin.Hash_Password.encode("utf-8")
    )

    if not is_password_correct:
        return exceptions.Unauthorized(
            description="Incorrect username/password combination"
        )
    token_payload = {"username": username}
    token = jwt_service.generate(token_payload)

    if token is None:
        return exceptions.InternalServerError(description="Login Failed")
    return {"token": token}


@Admin_Auth_API_blueprint.route("/api/auth/signup", methods=["POST"])
def sign_up():
    First_name, Last_name, Username, Password, Email_Id, IsAdmin, Gender, Phone_No, Address = (
        request.json["First_name"],
        request.json["Last_name"],
        request.json["Username"],
        request.json["Password"],
        request.json["Email_Id"],
        request.json["IsAdmin"],
        request.json["Gender"],
        request.json["Phone_No"],
        request.json["Address"]
    )
    print(f'request.headers.get("sign_up_key"): {request.headers.get("signupkey")}')
    print(f"sign_up_key: {sign_up_key}")
    if request.headers.get("signupkey") != sign_up_key:
        return exceptions.Unauthorized(description="Incorrect Key")
    password_hash = hashing_service.hash_bcrypt(Password.encode("utf-8")).decode(
        "utf-8"
    )

    admin = Agents(
        First_name, Last_name, Username, password_hash, Email_Id, IsAdmin, Gender, Phone_No, Address
    )
    db.session.add(admin)
    db.session.commit()
    return {"message": "Admin Created Successfully"}


@Admin_Auth_API_blueprint.route("/api/auth/is_logged_in")
def is_logged_in():
    return {"message": "token is valid"}

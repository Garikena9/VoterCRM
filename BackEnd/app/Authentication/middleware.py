from flask import Request
from .jwtservice import JWTService
from werkzeug import exceptions


class Middleware:
    def __init__(self, jwtservice: JWTService):
        self.unauthenticated_route_names = {"/admin/auth/login", "/admin/auth/signup","/admin/assemblyconstituency","/admin/add_constituency","/admin/delete_constituency","/admin/update_constituency_name"}
        self.jwtservice = jwtservice

    def auth(self, request: Request):
        print(f"request path: {request.path}")
        is_route_unauthenticated = request.path in self.unauthenticated_route_names
        print(f"is_route_unauthenticated: {is_route_unauthenticated}")

        if is_route_unauthenticated:
            print("returning none for unauthenticated")
            return None

        if "token" in request.headers:
            token = request.headers["token"]
            is_valid = self.jwtservice.is_valid(token)
            if is_valid:
                return None
            else:
                return exceptions.Unauthorized()
        return exceptions.Unauthorized()

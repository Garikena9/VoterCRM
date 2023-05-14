from Backend.app import application
from Backend.app.APIs.Admin_Auth_API import Admin_Auth_API_blueprint
from Backend.app.APIs.States_API import States_API_blueprint

# from Backend.app.APIs.Admin_Auth_API import *
# from Backend.app.APIs.States_API import *
from Backend.app.Models import *

application.register_blueprint(Admin_Auth_API_blueprint)
application.register_blueprint(States_API_blueprint)

if __name__ == "__main__":
    application.run(debug=True, port=8000)

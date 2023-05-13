from Backend import db


class Agents(db.Model):
    __tablename__ = "Agents"

    Agent_Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    First_name = db.Column(db.String(50), null=False)
    Last_name = db.Column(db.String(50), null=False)
    Username = db.Column(db.String(50), unique=True, null=False)
    Password = db.Column(db.String(50), null=False)
    Email_Id = db.Column(db.String(100), unique=True)
    IsAdmin = db.Column(db.Boolean, null=False)
    Gender = db.Column(db.String(10), null=False)
    Phone_No = db.Column(db.String(10))
    Address = db.Column(db.Text)

    def __init__(
        self,
        first_name,
        last_name,
        username,
        password,
        email_id,
        is_admin,
        gender,
        phone_no=None,
        address=None,
    ):
        self.First_name = first_name
        self.Last_name = last_name
        self.Username = username
        self.Password = password
        self.Email_Id = email_id
        self.IsAdmin = is_admin
        self.Gender = gender
        self.Phone_No = phone_no
        self.Address = address

from Backend.app import db


class Voters(db.Model):
    __tablename__ = "Voters"

    Voter_Row_ID = db.Column(db.Integer, primary_key=True)
    Voter_UID = db.Column(db.String(10), unique=True)
    Voter_Name = db.Column(db.String(100), null=False)
    Relative_Name = db.Column(db.String(100), null=False)
    Relation_Type = db.Column(db.Integer, db.ForeignKey("Relations.Relation_Id"), null=False)
    House_Number = db.Column(db.String(25), null=False)
    Age = db.Column(db.Integer, null=False)
    Gender = db.Column(db.String(10), null=False)
    Polling_Station_Code = db.Column(db.Integer, db.ForeignKey("PollingStations.Polling_Station_Id"))

    def __init__(self,Voter_Row_ID, Voter_UID, Voter_Name,Relative_Name,Relation_Type,House_Number,Age,Gender,Polling_Station_Code):
        self.Voter_Row_ID = Voter_Row_ID
        self.Voter_UID = Voter_UID
        self.Voter_Name = Voter_Name
        self.Relative_Name = Relative_Name
        self.Relation_Type = Relation_Type
        self.House_Number = House_Number
        self.Age = Age
        self.Gender = Gender
        self.Polling_Station_Code = Polling_Station_Code

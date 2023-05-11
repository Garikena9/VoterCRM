USE voter_crm;

CREATE TABLE Voters(
    Voter_Row_ID int PRIMARY KEY,
    Voter_UID char(10) UNIQUE,
    Voter_Name varchar(100) NOT NULL,
    Relative_Name VARCHAR(100) NOT NULL,
    Relation_Type int NOT NULL,
    House_Number varchar(25) NOT NULL,
    Age int NOT NULL,
    Gender varchar(10) NOT NULL,
    Polling_Station_Code int,
    FOREIGN KEY (Relation_Type) REFERENCES Relations(Relation_Id),
    FOREIGN KEY (Polling_Station_Code) REFERENCES PollingStations(Polling_Station_Id)
);



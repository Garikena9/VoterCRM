USE voter_crm;

CREATE TABLE Districts(
    District_Id int PRIMARY KEY,
    District_Name varchar(100) UNIQUE,
    District_No int NOT NULL,
    State_Code int,
    FOREIGN KEY (State_Code) REFERENCES States(State_Id)
);


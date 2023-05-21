USE voter_crm;

CREATE TABLE Logins(
      Id int PRIMARY KEY auto_increment,
      User_Id int NOT NULL,
      IP_Address varchar(25) NOT NULL,
      Device varchar(50) NOT NULL,
      Token text,
      Created_On datetime NOT NULL,
      Status varchar(25),
      Updated_On datetime NOT NULL,
      FOREIGN KEY (User_Id) REFERENCES Agents(Agent_Id)
);
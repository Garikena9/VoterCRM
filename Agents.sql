USE voter_crm;

CREATE TABLE Agents(
      Agent_Id int PRIMARY KEY auto_increment,
      First_name varchar(50) NOT NULL,
      Last_name varchar(50) NOT NULL,
      Username varchar(50) UNIQUE,
      Password varchar(50) NOT NULL,
      Email_Id varchar(100) UNIQUE,
      IsAdmin boolean NOT NULL,
      Gender varchar(10) NOT NULL,
      Phone_No char(10),
      Address text

);
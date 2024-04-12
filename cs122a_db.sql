DROP DATABASE IF EXISTS cs122a;
CREATE DATABASE cs122a;
USE cs122a;


-- User Table
CREATE TABLE Users (
    UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,
    FirstName VARCHAR(50),
    MiddleName VARCHAR(50),
    LastName VARCHAR(50)
);

CREATE TABLE UserEmail (
  UCINetID VARCHAR(20)  NOT NULL,
  Email    VARCHAR(511),
  PRIMARY KEY (UCINetID, Email),
  FOREIGN KEY (UCINetID) REFERENCES Users (UCINetID)
    ON DELETE CASCADE
);

-- Student Delta Table
CREATE TABLE Students (
    UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,
    FOREIGN KEY (UCINetID) REFERENCES Users(UCINetID)
      ON DELETE CASCADE
);

-- Administrator Delta Table
CREATE TABLE Administrators (
    UCINetID VARCHAR(20) PRIMARY KEY NOT NULL,
    FOREIGN KEY (UCINetID) REFERENCES Users(UCINetID)
      ON DELETE CASCADE
);




-- Course Table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY NOT NULL,
    Title VARCHAR(100),
    Quarter VARCHAR(20)
);

-- Project Table
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(100),
    Description TEXT,
    CourseID INT NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Machine Table
CREATE TABLE Machines (
    MachineID INT PRIMARY KEY NOT NULL,
    Hostname VARCHAR(255),
    IPAddress VARCHAR(15),
    OperationalStatus VARCHAR(50),
    Location VARCHAR(255)
);





-- Use Relationship Table
CREATE TABLE StudentUseMachinesInProject (
    ProjectID INT,
    StudentUCINetID VARCHAR(20),
    MachineID INT,
    StartDate DATE,
    EndDate DATE,
    PRIMARY KEY (ProjectID, StudentUCINetID, MachineID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (StudentUCINetID) REFERENCES Students(UCINetID),
    FOREIGN KEY (MachineID) REFERENCES Machines(MachineID)
);

-- Administrator Machine Management Table

CREATE TABLE AdministratorManageMachines (
    AdministratorUCINetID VARCHAR(20),
    MachineID INT,
    PRIMARY KEY (AdministratorUCINetID, MachineID),
    FOREIGN KEY (AdministratorUCINetID) REFERENCES Administrators(UCINetID),
    FOREIGN KEY (MachineID) REFERENCES Machines(MachineID)
);



CREATE TABLE Address (
  id int NOT NULL AUTO_INCREMENT,
  city VARCHAR(50) NOT NULL,
  street VARCHAR(50) NOT NULL,
  home VARCHAR(50) NOT NULL,
  CONSTRAINT PK_Address PRIMARY KEY (id)
);

CREATE TABLE FullName
(
  id int NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  middle_name VARCHAR(50) NOT NULL DEFAULT '',
  last_name VARCHAR(50) NOT NULL,
  CONSTRAINT PK_FullName PRIMARY KEY (id)
);

CREATE TABLE Contact 
(
  id int NOT NULL AUTO_INCREMENT,
  tel varchar(20) NOT NULL UNIQUE CHECK (tel REGEXP '^[\+]?[[:digit:]]{3,15}$'),
  email varchar(50) NOT NULL UNIQUE CHECK (email REGEXP '^[^@]+@[^@]+\.[^@]{2,}$'),
  fax varchar(50) UNIQUE,
  CONSTRAINT PK_Contact PRIMARY KEY (id)
);


CREATE TABLE Center
(
  id int NOT NULL AUTO_INCREMENT,
  address_id int NOT NULL UNIQUE,
  contact_id int NOT NULL  UNIQUE,
  CONSTRAINT PK_Center PRIMARY KEY (id),
  CONSTRAINT FK_Center_Address FOREIGN KEY (address_id) REFERENCES Address(id),
  CONSTRAINT FK_Center_Contact FOREIGN KEY (contact_id) REFERENCES Contact(id)
);

CREATE TABLE Patient
(
  id int NOT NULL AUTO_INCREMENT,
  fullname_id int NOT NULL,
  address_id int NOT NULL,
  contact_id int NOT NULL UNIQUE,
  sex ENUM('m', 'w') NOT NULL,
  registration_date DATE NOT NULL, /* data_check trigger for default*/
  CONSTRAINT PK_Patient PRIMARY KEY (id),
  CONSTRAINT FK_Patient_Fullname FOREIGN KEY (fullname_id) REFERENCES FullName(id),
  CONSTRAINT FK_Patient_Address FOREIGN KEY (address_id) REFERENCES Address(id),
  CONSTRAINT FK_Patient_Contact FOREIGN KEY (contact_id) REFERENCES Contact(id)
);

CREATE TABLE PatientCenter 
(
  center_id int NOT NULL,
  patient_id int NOT NULL,
  CONSTRAINT PK_PatientCenter PRIMARY KEY (center_id, patient_id)
);

CREATE TABLE Stuff
(
  id int NOT NULL AUTO_INCREMENT,
  fullname_id int NOT NULL,
  address_id int NOT NULL,
  contact_id int NOT NULL UNIQUE,
  iin CHAR(6) NOT NULL UNIQUE,
  sex ENUM('m', 'w') NOT NULL,
  position varchar(50) NOT NULL,
  salary DECIMAL(10, 2) NOT NULL CHECK(salary >= 0),
  center_id int NOT NULL,
  role ENUM('Admin', 'Manager', 'Stuff') NOT NULL,
  CONSTRAINT PK_Stuff PRIMARY KEY (id),
  CONSTRAINT FK_Stuff_FullName FOREIGN KEY (fullname_id) REFERENCES FullName(id),
  CONSTRAINT FK_Stuff_Adress FOREIGN KEY (address_id) REFERENCES Address(id),
  CONSTRAINT FK_Stuff_Contact FOREIGN KEY (contact_id) REFERENCES Contact(id),
  CONSTRAINT FK_Stuff_Center FOREIGN KEY (center_id) REFERENCES Center(id)
);

CREATE TABLE StockItem
(
  id int NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE,
  description TEXT NOT NULL,
  cost decimal(10, 2) NOT NULL CHECK(cost >= 0),
  quantity int NOT NULL CHECK(quantity >= 0),
  center_id int NOT NULL,
  CONSTRAINT PK_StockItem PRIMARY KEY (id),
  CONSTRAINT FK_StockItem_Center FOREIGN KEY (center_id) REFERENCES Center(id)
);

CREATE TABLE StockPharmacy
(
  id int NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE,
  description TEXT NOT NULL,
  dosage TEXT NOT NULL,
  on_prescription ENUM('yes', 'no') NOT NULL,
  cost decimal(10, 2) NOT NULL CHECK(cost >= 0),
  quantity int NOT NULL CHECK(quantity >= 0),
  center_id int NOT NULL,
  CONSTRAINT PK_StockPharmacy PRIMARY KEY (id),
  CONSTRAINT FK_StockPharmacy_Center FOREIGN KEY (center_id) REFERENCES Center(id)
);

CREATE TABLE CryogenicChamber
(
  id int NOT NULL AUTO_INCREMENT,
  size ENUM('head', 'small', 'medium', 'large') NOT NULL,
  status ENUM('occupied', 'free') NOT NULL DEFAULT 'free',
  patient_id int UNIQUE,
  center_id int NOT NULL,
  CONSTRAINT PK_CryogenicChamber PRIMARY KEY (id),
  CONSTRAINT FK_CryogenicChamber_Patient FOREIGN KEY (patient_id) REFERENCES Patient(id),
  CONSTRAINT FK_CryogenicChamber_Center FOREIGN KEY (center_id) REFERENCES Center(id)
);

CREATE TABLE Examination
(
  id int NOT NULL AUTO_INCREMENT,
  time DATETIME NOT NULL, /* data_check trigger for default*/
  doctor_id int NOT NULL,
  patient_id int NOT NULL,
  results TEXT NOT NULL,
  CONSTRAINT PK_Examination PRIMARY KEY (id),
  CONSTRAINT FK_Examination_Stuff FOREIGN KEY (doctor_id) REFERENCES Stuff(id),
  CONSTRAINT FK_Examination_Patient FOREIGN KEY (patient_id) REFERENCES Patient(id)
);

CREATE TABLE Invoice
(
  id int NOT NULL AUTO_INCREMENT,
  cost DECIMAL(10, 2) NOT NULL CHECK(cost >= 0),
  date_issue DATE NOT NULL, /* data_check trigger for default*/
  date_paid DATE, /* data_check trigger to check*/
  payment_method ENUM('card', 'cash', 'check'),
  CONSTRAINT PK_Invoice PRIMARY KEY (id)
);

CREATE TABLE Treatment
(
  id int NOT NULL AUTO_INCREMENT,
  description TEXT NOT NULL,
  doctor_id int NOT NULL,
  invoice_id int NOT NULL UNIQUE,
  examination_id int NOT NULL,
  CONSTRAINT PK_Treatment PRIMARY KEY (id),
  CONSTRAINT FK_Treatment_Doctor FOREIGN KEY (doctor_id) REFERENCES Stuff(id),
  CONSTRAINT FK_Treatment_Invoice FOREIGN KEY (invoice_id) REFERENCES Invoice(id),
  CONSTRAINT FK_Treatment_Examination FOREIGN KEY (examination_id) REFERENCES Examination(id)
);


CREATE TABLE Artist (
	Name VARCHAR(50) NOT NULL,
	Phone VARCHAR(20) NOT NULL,
	Address VARCHAR(255),
	Birth_place VARCHAR(50),
	Age INT,
	Style_of_art VARCHAR(255),
	PRIMARY KEY (Name),
	UNIQUE (Name)
);

CREATE TABLE Art_work (
	Artist VARCHAR(50) NOT NULL,
	Title VARCHAR(100) NOT NULL,
	Type_of_art VARCHAR(255) NOT NULL,
	Date_of_creation VARCHAR(10) NOT NULL,
	Price VARCHAR(8) NOT NULL,
	Location VARCHAR(50) NOT NULL,
	UNIQUE (Title),
	FOREIGN KEY (Artist) REFERENCES Artist(Name)
);

CREATE TABLE Customer (
	Customer_number INT NOT NULL,
	Phone VARCHAR(20) NOT NULL,
	Art_preferences VARCHAR(255) NOT NULL
);

CREATE TABLE Art_shows (
	Date_and_time VARCHAR(17) NOT NULL,
	Location VARCHAR(50) NOT NULL,
	Contact_phone VARCHAR(20) NOT NULL,
	Artist VARCHAR(50) NOT NULL,
	FOREIGN KEY (Artist) REFERENCES Artist(Name)
);
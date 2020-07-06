This python Program is to get the open source data about Covid-19 India cases from "http://api.covid19india.org" in your MySQL Database.

Inputs for the program:
	1. Enter the .json page URL
	   Example : http://api.covid19india.org/raw_data7.json

Things to do before running the code:
1.Create a new database in mysql , name Your database  as 'covid'.
2.Create a Table with the following querry

CREATE TABLE `table1`(
`PNo` INTEGER PRIMARY KEY,
`Age` INTEGER,
`Gender` TEXT,
`City` TEXT,
`State` TEXT,
`Date` TEXT
)

** If any problem arises change the type of `Age` as INTEGER **


**NOTE
Install all required Library
I have written the code to get the following "Entry Id, Age, Gender, City, State, Date of report" of the patient.
If you want some more info, you can edit the code.
 

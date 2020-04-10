import sqlite3 as sql

def applicationDoctor():
	data= sql.connect("Hospital.db")
	dataCursor = data.cursor()
	dataCursor.execute('''CREATE TABLE IF NOT EXISTS hospital_doctordata(ID INT PRIMARY KEY NOT NULL,
		FIRSTNAME TEXT NOT NULL, 
		SECONDNAME TEXT NOT NULL, 
		SPECIALIZATION TEXT NOT NULL, 
		AVAILABILITY TEXT NOT NULL, 
		AGE INT NOT NULL)''')
	data.commit()
	data.close()


def AddDoctorDetails(Id,firstName,secondName,Specialization,Availability,Age):
	data = sql.connect("Hospital.db")
	dataCursor = data.cursor()
	dataCursor.execute('''INSERT INTO hospital_doctordata(ID,FIRSTNAME,SECONDNAME,
		SPECIALIZATION,AVAILABILITY,AGE)VALUES(?,?,?,?,?,?)''',(Id,firstName,secondName,Specialization,Availability,Age))

	data.commit()
	data.close()

def DeleteDoctorDetails(No):
	data = sql.connect("Hospital.db")
	dataCursor = data.cursor()
	dataCursor.execute('''DELETE from hospital_doctordata WHERE ID = ?''',(No,))
	data.commit()
	data.close()

def DisplayingDoctorDetails():
	data = sql.connect("Hospital.db")
	dataCursor = data.cursor()
	dataCursor.execute('''SELECT * FROM hospital_doctordata''')
	docData = dataCursor.fetchall()
	return docData

def UpdateDoctorDetails(Id,firstName,secondName,Specialization,Availability,Age):
	data = sql.connect("Hospital.db")
	dataCursor = data.cursor()
	dataCursor.execute('''UPDATE hospital_doctordata SET FIRSTNAME = ?,SECONDNAME = ?,SPECIALIZATION = ?,
		AVAILABILITY = ?,AGE = ? WHERE ID = ?''',(firstName,secondName,Specialization,Availability,Age,Id))
	data.commit()
	data.close()


applicationDoctor()




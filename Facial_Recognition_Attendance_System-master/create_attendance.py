import csv
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='STUDENTS_DB')
mycursor = mydb.cursor()

def addData():
	mycursor.execute("select * from student")

	name = []
	id = []

	for row in mycursor:
		profile = row
		id.append(profile[0])
		name.append(profile[1])

	raw_data = {'Id':id,'Name':name}
	return raw_data


raw_data = addData()
df = pd.DataFrame(raw_data,columns = ['Id','Name'])
df.to_csv('attendance.csv',index=False)


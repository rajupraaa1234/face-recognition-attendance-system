import cv2
import numpy as np
import mysql.connector

# Connecting mysql with python
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="STUDENTS_DB")
mycursor = mydb.cursor()

def insertOrUpdate(Id,Name):
	cmd = "SELECT * FROM student WHERE Roll="+str(Id)
	parmas = (Id,Name)
	mycursor.execute(cmd)

	isRecordExist = 0

	for row in mycursor:
		isRecordExist = 1

	if isRecordExist==1:
		print("ID already exists")
		return False
	else:
		Name = "\'" + Name + "\'"
		cmd = "insert into student(Roll, name) values(" +str(Id) + "," + str(Name) + ");"
		mycursor.execute(cmd)
		mydb.commit()
		print(mycursor.rowcount, "record inserted.")
		return True

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

ID = input("Enter your id ")
name = input("Enter your name ")
flag = insertOrUpdate(ID,name)

count = 0
while True and flag:
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray,1.5,5)
	for x,y,w,h in faces:
		count += 1
		cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
		cv2.imwrite("dataset/user"+ str(ID) +'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])
	cv2.imshow("image",gray)
	if cv2.waitKey(3)==13 or count>500:
		break

cam.release()
cv2.destroyAllWindows()


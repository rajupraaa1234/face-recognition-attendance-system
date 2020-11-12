import cv2
import mysql.connector
cascade_Classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='STUDENTS_DB')
mycursor = mydb.cursor()


def getProfile(id):
	cmd = "SELECT * FROM student WHERE Roll="+str(id)
	mycursor.execute(cmd)
	profile = None

	for row in mycursor:
		profile = row
	return profile

cam = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainFile.yml')
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = cascade_Classifier.detectMultiScale(gray,1.5,5)


	for x,y,w,h in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
		id,conf = recognizer.predict(gray[y:y+h,x:x+w])
		if(conf>=45 and conf<=85):
			profile = getProfile(id)
			if(profile!=None):
				# cv2.putText(frame,profile[0],(x,y+h+60),font,3,(0,255,0))
				cv2.putText(frame,profile[1],(x,y+h+100),font,3,(0,255,0))
			
	cv2.imshow('image', frame)
	key = cv2.waitKey(1)
	if key == 13:
		break

cam.release()
cv2.destroyAllWindows()


import cv2


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

while True:
	ret, frame = cam.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray,1.5,5)
	for x,y,w,h in faces:
		cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
	cv2.imshow("image",gray)

	if cv2.waitKey(3)==13:
		break

cam.release()
cv2.destroyAllWindows()
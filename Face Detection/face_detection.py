import cv2

img = cv2.imread("Resources/barack.jpg")
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Output", img)
cv2.waitKey(0)
#imported modules -
import cv2
import winsound
#declaring variables to capture
cam = cv2.VideoCapture(0)
while cam.isOpened():
#declaring the frames -
    ret, Frame1 = cam.read()
    ret, Frame2 = cam.read()
#some functions of opencv - 
    diff = cv2.absdiff(Frame1, Frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3) 
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(Frame1, contours, -1, (0, 255, 0), 2) 
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(Frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
#to stop the cam -
    if cv2.waitKey(10) == ord('x'):
        break
    cv2.imshow('Nav Cam', Frame1)

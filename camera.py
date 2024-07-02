import cv2
import time

cam = cv2.VideoCapture(0)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))
print("{}x{} {}fps".format(width, height, fps))

if not cam.isOpened():
    print("Camera is not available")
    exit()

while True:
    ret, img = cam.read()
    key = cv2.waitKey(1)
    if not ret:
        print("Camera is not available")
        break
    
    cv2.imshow('Camera', img)    
    if key == 27:    #ESC
        break  

    elif key == 13:    #Enter
        file_name = ("ScreenShot "+time.ctime(time.time())+ ".jpeg")
        image = cv2.imwrite(file_name, img)             
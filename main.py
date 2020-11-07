import pyautogui
from cv2 import cv2
import numpy as np


resolution = (1366, 768) #Screen Resolution

codec = cv2.VideoWriter_fourcc(*"XVID") #codex



out = cv2.VideoWriter("Recorded.avi", codec, 60, resolution)

cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270)

while True:
    img = pyautogui.screenshot() #capturing screenshot
    frame = np.array(img) #converting the image into numpy array representation 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting the BGR image into RGB image
    out.write(frame) #writing the RBG image to file
    cv2.imshow('Recording', frame) #display screen/frame being recorded
    if cv2.waitKey(1) == ord('q'): #Wait for the user to press 'q' key to stop the recording
        break

out.release()
cv2.destroyAllWindows()





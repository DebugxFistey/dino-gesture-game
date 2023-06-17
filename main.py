import cv2
import numpy as np
import subprocess
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(detectionCon=0.8, maxHands=1)
subprocess.call(['xdotool', 'keydown', 'space'])  # Simulate initial keydown
time.sleep(2.0)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    keyPressed = False
    spacePressed = False
    hands, img = detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)

    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        print(fingerUp)

        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Finger Count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Jumping', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            subprocess.call(['xdotool', 'keydown', 'space'])  # Simulate key press
            spacePressed = True
            keyPressed = True

        if not keyPressed:
            subprocess.call(['xdotool', 'keyup', 'space'])  # Simulate key release

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

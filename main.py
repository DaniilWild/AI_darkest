import cv2
import numpy as np
import pyautogui
import time

SCREEN_SIZE = (1920, 1080)
fource = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fource, 20.0, (SCREEN_SIZE))

fps = 30
prev = 0


z1 = pygetwindow.getAllTitles()
time.sleep(1)
print(len(z1))
while True:
    time_elapsed = time.time()-prev
    img = pyautogui.screenshot(region=(0,0, 300, 400))

    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    cv2.imshow('', frame)

    key = cv2.waitKey(1000)
    if key == 27 :
        break
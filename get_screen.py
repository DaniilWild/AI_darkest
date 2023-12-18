from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import os
import cv2
import time
from os import listdir


buffer_filename = 'buffer.jpg'

def capture_window(window_name = 'Darkest Dungeon'):
    succes, img = False, None
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)

    for window in window_list:
        try:
            if window_name.lower()  == window['kCGWindowName'].lower():
                os.system('screencapture -l %s %s' %(window['kCGWindowNumber'], buffer_filename))
                succes, img = True, cv2.imread(buffer_filename)
                break
        except:
            continue
    else:
        raise Exception('Window %s not found.'%window_name)
    return succes, img

def clear_caсhe():
    global_path = os.path.abspath(os.curdir)
    [os.remove(f) for f in listdir(global_path) if buffer_filename in f]




if __name__ == "__main__":
    prev = time.time()
    clear_caсhe()

    fps = 10

    while True:
        time_elapsed = time.time() - prev

        if time_elapsed > 1.0 / fps:
            prev = time.time()

            succes, img = capture_window('Darkest Dungeon')
            cv2.imwrite(buffer_filename, img)
            # if succes:
            #
            #
            #     cv2.imshow('', img)

        key = cv2.waitKey(4000)
        if key == 27:
            break
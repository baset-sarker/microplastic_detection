import numpy as np
import cv2 as cv


def calculate_framerate(frame_rate_calc,t1,freq):
    print('FPS: {0:.2f}'.format(frame_rate_calc))
    # Calculate framerate
    t2 = cv.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc= 1/time1
    return frame_rate_calc

#freq = cv2.getTickFrequency()
# inside while loop   t1 = cv2.getTickCount()
# frame_rate_calc = calculate_framerate(frame_rate_calc,t1,freq)

cap = cv.VideoCapture(2)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

frame_rate_calc = 1
freq = cv.getTickFrequency()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    t1 = cv.getTickCount()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
   # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    from datetime import datetime
    file_name = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')
    frame_rate_calc = calculate_framerate(frame_rate_calc,t1,freq)
    
    #cv.imwrite("images/"+file_name+'.jpg', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
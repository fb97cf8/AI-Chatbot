import cv2

for i in range(100):
    cap = cv2.VideoCapture('Animation/idle.mp4')
    frameTime = 15
    while(cap.isOpened()):
        result,frame = cap.read()
        if result == True:
            frame = cv2.resize(frame,(1280,720))
            cv2.imshow('AI PERSON!', frame)
            if cv2.waitKey(frameTime) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()


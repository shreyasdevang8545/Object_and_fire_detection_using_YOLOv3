import cv2
import playsound

vid = cv2.VideoCapture(0) #use 0 for capturing video from main webcam
                        
fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

while True:
    _, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # To convert frame into gray color
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5) # to provide frame resolution
#fire detection program
    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        print("Fire detected") #prints the content when fire detected.
        playsound('alarm-sound.mp3') #play audio when fire detected.

    cv2.imshow("Image", frame) #output frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
vid.release()
cv2.destroyAllWindows()

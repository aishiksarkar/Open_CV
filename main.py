#These lines import necessary libraries cv2 for computer vision, mediapipe for hand tracking and gesture recognition, and time for adding a delay.
import cv2 #
import mediapipe as mp
import time
#import new as cnt
 
#This line introduces a delay of 2 seconds before the code execution starts.
time.sleep(2.0)

#These lines create instances of mp.solutions.drawing_utils and mp.solutions.hands classes, which are used later for drawing hand landmarks on the video frames.
mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands


#This line creates a list of finger tip landmark IDs used to count the number of fingers raised.
tipIds=[4,8,12,16,20]

#This line creates an instance of the cv2.VideoCapture class, which captures video from the default camera.
video=cv2.VideoCapture(0)

#This line creates a context manager to handle the hand tracking using the mp_hand.Hands class with minimum detection and tracking confidence of 0.5.
with mp_hand.Hands(min_detection_confidence=0.5,
               min_tracking_confidence=0.5) as hands:
    
    while True:
        ret,image=video.read()#This line captures the current frame from the video and stores it in the image variable. The ret variable indicates if the frame was successfully captured.
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)#These lines convert the color space of the image from BGR to RGB and then disable write access to the image data to make it read-only.
        image.flags.writeable=False
        results=hands.process(image)#This line uses the hands.process method to detect hand landmarks in the current video frame.
        image.flags.writeable=True#These lines enable write access to the image data again and then convert the color space back to BGR.
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        #These lines extract the landmarks of all hands in the current video frame using the results.multi_hand_landmarks attribute. It then extracts the x and y coordinates of each landmark and stores them in the lmList list. Additionally, it uses mp_draw.draw_landmarks method to draw landmarks on the frame.
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)#getting the coordinates
                    lmList.append([id,cx,cy])#For storing the  Cartesian coordinates..
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers=[]#These lines count the number of fingers raised by comparing the y-coordinates of the finger tip landmarks to the y-coordinates of the landmarks of the fingers
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total=fingers.count(1)#Counting fingers!
            #cnt.led(total) # The Arduino Connection!
            if total==0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "Danger", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                
            elif total==1:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "Water?", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==2:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "Hungry", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==3:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "Listen", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==4:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "Washroom!", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==5:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "Scared!", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
        cv2.imshow("Frame",image)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
video.release()
cv2.destroyAllWindows()


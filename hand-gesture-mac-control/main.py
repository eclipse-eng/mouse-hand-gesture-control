import pyautogui
import cv2
from math import hypot
import mediapipe as mp
from numpy import interp

screen_width, screen_height = pyautogui.size()

mp_hands = mp.solutions.hands           
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)



#open webcam (0 for default camera,if not 0 try 1,2 etc) 
cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
alpha = 0.2  # smoothing factor between 0 and 1

while True:
    success, frame = cap.read()
    if not success:
        break

    #convert the frame
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame, (640, 480))
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    


    #process the frame
    results = hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks :
            #print(hand_landmarks.landmark[8])
            thumb_tip = hand_landmarks.landmark[8]
            index_tip = hand_landmarks.landmark[4]

            height, width, _ = frame.shape
            
            screen_x = interp(index_tip.x, [0, 1], [0, screen_width])
            screen_y = interp(index_tip.y, [0, 1], [0, screen_height])


            # Convert normalized landmarks to pixel positions
            x1, y1 = int(index_tip.x * width), int(index_tip.y * height)
            x2, y2 = int(thumb_tip.x * width), int(thumb_tip.y * height)

            # Calculate Euclidean distance
            distance = hypot(x2 - x1, y2 - y1)
            print(distance)

            #smoothing
            smooth_x = prev_x + (screen_x - prev_x ) * alpha
            smooth_y = prev_y + (screen_y - prev_y) * alpha

            pyautogui.moveTo(screen_x , screen_y)
            prev_x, prev_y = smooth_x, smooth_y


            #clicking
            if distance < 40 :
                pyautogui.click()
                print('click!')
            

            
            #draw circle
            cv2.circle(frame, (int(x1), int(y1)), 10, (255,0,0),-1)
            cv2.circle(frame, (int(x2), int(y2)), 10, (255,0,0),-1)



    #show the frame
    cv2.imshow('webcam feed',frame)
    #press 'q' on the 'webcam feed' window to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

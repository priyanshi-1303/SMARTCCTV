import cv2
import os
from datetime import datetime

def in_out():
    cap = cv2.VideoCapture(0)
    
    # Initialize right and left directions as booleans
    right, left = False, False

    # Ensure the visitor directories exist
    os.makedirs("visitors/in", exist_ok=True)
    os.makedirs("visitors/out", exist_ok=True)

    while True:
        # Capture two frames for motion detection
        _, frame1 = cap.read()
        if frame1 is None:  # Check if frame is captured correctly
            print("Error: Failed to capture frame.")
            break
        frame1 = cv2.flip(frame1, 1)  # Flip the frame horizontally
        
        _, frame2 = cap.read()
        if frame2 is None:  # Check if second frame is captured correctly
            print("Error: Failed to capture second frame.")
            break
        frame2 = cv2.flip(frame2, 1)  # Flip the second frame
        
        # Calculate the difference between the frames
        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.blur(diff, (5,5))  # Apply blur to reduce noise
        
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Convert the diff to grayscale
        
        # Apply threshold to get a binary image
        _, threshd = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
        
        # Find contours in the thresholded image
        contr, _ = cv2.findContours(threshd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        x = 300  # Initialize a default value for x
        
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)  # Get the largest contour
            x, y, w, h = cv2.boundingRect(max_cnt)  # Get the bounding box of the largest contour
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)  # Draw a rectangle around the motion
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        
        # Direction check logic
        if not right and not left:  # If no direction has been assigned yet
            if x > 500:  # If the detected motion is on the right
                right = True
            elif x < 200:  # If the detected motion is on the left
                left = True
                
        elif right:
            if x < 200:  # If the motion crosses into the left area
                print("Motion detected: Moving to left")
                right, left = False, False
                cv2.imwrite(f"visitors/in/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg", frame1)  # Save the image in 'in' folder
            
        elif left:
            if x > 500:  # If the motion crosses into the right area
                print("Motion detected: Moving to right")
                right, left = False, False
                cv2.imwrite(f"visitors/out/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg", frame1)  # Save the image in 'out' folder
            
        # Display the frame
        cv2.imshow("Camera Feed", frame1)
        
        k = cv2.waitKey(1)  # Wait for a key press
        if k == 27:  # Press 'Esc' to exit
            cap.release()  # Release the camera
            cv2.destroyAllWindows()  # Close all OpenCV windows
            break
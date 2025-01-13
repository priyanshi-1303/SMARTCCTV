import cv2
import os
from datetime import datetime

def record():
    # Ensure the 'recordings' folder exists
    if not os.path.exists('recordings'):
        os.makedirs('recordings')
    
    cap = cv2.VideoCapture(0)

    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_file = f'recordings/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.avi'
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture video. Exiting...")
            break

        # Add timestamp to the video frame
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timestamp, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

        # Write the frame to the video file
        out.write(frame)

        # Display the video feed
        cv2.imshow("Press 'Esc' to stop recording", frame)

        # Stop recording when 'Esc' is pressed
        if cv2.waitKey(1) == 27:
            print(f"Recording saved to: {output_file}")
            break

    # Release resources
    cap.release()
    out.release()
    #cv2.destroyAllWindows()
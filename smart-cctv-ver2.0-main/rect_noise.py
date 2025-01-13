import cv2
import winsound  # For beep sound (works on Windows)

# Global variables
donel = False
doner = False
x1, y1, x2, y2 = 0, 0, 0, 0

# Mouse callback function for selecting the region
def select(event, x, y, flags, param):
    global x1, x2, y1, y2, donel, doner
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        donel = True
    elif event == cv2.EVENT_RBUTTONDOWN:
        x2, y2 = x, y
        doner = True

# Function for detecting noise/motion
def rect_noise():
    global x1, x2, y1, y2, donel, doner
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("Select Region")
    cv2.setMouseCallback("Select Region", select)

    print("Select the region using left and right mouse buttons.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video.")
            break

        cv2.imshow("Select Region", frame)

        if donel and doner:
            print("Region selected.")
            break

        if cv2.waitKey(1) == 27:  # Exit on ESC key
            print("Selection cancelled.")
            cap.release()
            cv2.destroyAllWindows()
            return

    while True:
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        if not ret:
            print("Failed to capture video.")
            break

        frame1_roi = frame1[y1:y2, x1:x2]
        frame2_roi = frame2[y1:y2, x1:x2]

        diff = cv2.absdiff(frame2_roi, frame1_roi)
        diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff_blur = cv2.blur(diff_gray, (9, 9))
        _, thresh = cv2.threshold(diff_blur, 50, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame1, (x + x1, y + y1), (x + w + x1, y + h + y1), (0, 255, 0), 2)
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

            # Play a beep sound
            winsound.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 500 ms
        else:
            cv2.putText(frame1, "NO MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.imshow("Noise Detection (Press ESC to exit)", frame1)

        if cv2.waitKey(1) == 27:  # Exit on ESC key
            break

    cap.release()
    #cv2.destroyAllWindows()

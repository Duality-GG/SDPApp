import cv2

# Typically the device index for your webcam is 0, but it might be a different number
# You might have to try different numbers if 0 does not work
cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Display the resulting frame
        cv2.imshow('USB Webcam', frame)

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Unable to read frame. Exiting...")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

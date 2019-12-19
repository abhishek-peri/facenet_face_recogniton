# Import OpenCV2 for image processing
import cv2
import os

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
face_id=input('enter your id')

# Start capturing video 
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize sample face image
count = 0

assure_path_exists("dataset_new/")
os.makedirs("dataset_new/{}".format(face_id))
# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    cv2.waitKey(10000)
    image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite("dataset_new/{}/User.".format(face_id) + str(face_id) + '.' + str(count) + ".jpg", image_frame)

    count += 1

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count>=50:
        print("Successfully Captured")
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()

import cv2

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# The file haarcascade_frontalface_default.xml is a pre-trained face detection model provided by OpenCV.
# Read the input image
img = cv2.imread("opencv/img.jpg")

# Convert to grayscale because detection works on gray images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import sys

# get the features for face from the file and pass it to the Cascade Classifier
# returns a class
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# get the features for eyes from the file and pass it to the Cascade Classifier
# returns a class
eyes_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
# read the image
img = cv2.imread('mypic4.jpg')
# resize the image if needed
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) #(image, (0, 0), reduce_width_by, reduce_height_by)
# convert it to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect the objects resembling faces
faces = face_cascade.detectMultiScale(gray, 1.5, 6) #(image,scale_factor, minm_no_of_neighbours)
# print(faces)
# ensure we have only two people in the image since we will be performing swapping
if len(faces) != 2:
    sys.exit('Please provide image with 2 faces')
# get the coordinates of the detected faces
x1, y1, w1, h1 = faces[0]
x2, y2, w2, h2 = faces[1]

# get eyes for the first face
face_color1 = img[y1: y1 + h1, x1: x1 + w1]
face_gray1 = gray[y1: y1 + h1, x1: x1 + w1]
eyes = eyes_cascade.detectMultiScale(face_gray1, 1.11, 4)
x3, y3, w3, h3 = eyes[0]
x4, y4, w4, h4 = eyes[1]
# carve out the eyes
eye_color1 = face_color1[y3: y3 + h3, x3: x3 + w3]
eye_color2 = face_color1[y4: y4 + h4, x4: x4 + w4]
#print("eye1",w3,h3) # coordinates for eye1
#print("eye2",w4,h4) # coordinates for eye2

# get eyes for the second face
face_color2 = img[y2: y2 + h2, x2: x2 + w2]
face_gray2 = gray[y2: y2 + h2, x2: x2 + w2]
eyes = eyes_cascade.detectMultiScale(face_gray2, 1.11, 4)
x5, y5, w5, h5 = eyes[0]
x6, y6, w6, h6 = eyes[1]
eye_color3 = face_color2[y5: y5 + h5, x5: x5 + w5]
eye_color4 = face_color2[y6: y6 + h6, x6: x6 + w6]
#print("eye3",w5,h5) # coordinates for eye3
#print("eye4",w6,h6) # coordinates for eye4

# resize the eyes
eye_color1 = cv2.resize(eye_color1, (w5, h5))
eye_color3 = cv2.resize(eye_color3, (w3, h3))
eye_color4 = cv2.resize(eye_color4, (w4, h4))
eye_color2 = cv2.resize(eye_color2, (w6, h6))

# swap the eyes
face_color1[y3: y3 + h3, x3: x3 + w3] = eye_color3
face_color2[y5: y5 + h5, x5: x5 + w5] = eye_color1
face_color1[y4: y4 + h4, x4: x4 + w4] = eye_color4
face_color2[y6: y6 + h6, x6: x6 + w6] = eye_color2

# show the image
cv2.imshow("Swapped Eyes",img)
# hold the window
cv2.waitKey(0)
# destroy all windows
cv2.destroyAllWindows()

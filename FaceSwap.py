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
faces = face_cascade.detectMultiScale(gray, 1.05, 6) #(image,scale_factor, minm_no_of_neighbours)
# print(faces)
# ensure we have only two people in the image since we will be performing swapping
if len(faces) != 2:
    sys.exit('Please provide image with 2 faces')
# get the coordinates of the detected faces
x1, y1, w1, h1 = faces[0]
x2, y2, w2, h2 = faces[1]
# get the first detected face using image slicing
face1 = img[y1: y1 + h1,x1: x1 + w1]
# get the second detected face using image slicing
face2 = img[y2: y2 + h2,x2: x2 + w2]
#resize the images so that they can be swapped
face1 = cv2.resize(face1, (w2, h2)) # face1 is (305,305)
face2 = cv2.resize(face2, (w1,h1))  # face2 is (269,269)
#swap the faces
# note you have to swap the actual coordinates and not the variables face1 and face2
img[y1: y1 + h1, x1: x1 + w1] = face2
img[y2: y2 + h2,x2: x2 + w2] = face1
# show the image
cv2.imshow("Swapped Faces", img)
# hold the window
cv2.waitKey(0)
# destroy all windows
cv2.destroyAllWindows()

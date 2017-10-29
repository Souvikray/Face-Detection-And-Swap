import cv2

# get the features for face from the file and pass it to the Cascade Classifier
# returns a class
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# get the features for eyes from the file and pass it to the Cascade Classifier
# returns a class
eyes_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
# read the image
img = cv2.imread('mypic3.png')
# resize the image if needed
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) #(image, (0, 0), reduce_width_by, reduce_height_by)
# convert it to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect the objects resembling faces
faces = face_cascade.detectMultiScale(gray, 1.5, 4) #(image,scale_factor, minm_no_of_neighbours)
# print(faces)

for face in faces:
    # we can check the dimension of the detected face
    # print(face)

    # get the coordinate of the detected face
    x, y, w, h = face
    # draw the rectangle on the image
    cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 2) # (image, top_left_ corner, bottom_right_corner, color_of_rectangle, color_thickness)
    # the idea is instead of looking at the entire image for eyes,we can just look at the detected faces
    # and try to search for eye regions on those faces
    # get the detected face using image slicing
    face_color = img[y: y + h, x: x + w]
    face_gray = gray[y: y + h, x: x + w]
    #cv2.imshow("Sliced out face", face_gray)
    eyes = eyes_cascade.detectMultiScale(face_gray, 1.11, 4)
    for eye in eyes:
        # get the coordinate of the detected eye
        x, y, w, h = eye
        # draw a rectangle on the eyes of the face
        cv2.rectangle(face_color, (x, y), (x + w, y + h), (255, 0, 0), 2)

# show the image
cv2.imshow("Detected Faces",img)
# hold the window
cv2.waitKey(0)
# destroy all windows
cv2.destroyAllWindows()

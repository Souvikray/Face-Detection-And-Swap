import cv2

# get the features from the file and pass it to the Cascade Classifier
# returns a class
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# read the image
img = cv2.imread('mypic3.png')
# resize the image if needed
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) #(image, (0, 0), reduce_width_by, reduce_height_by)
# convert it to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect the objects resembling faces
faces = face_cascade.detectMultiScale(gray,1.5,3) #(image,scale_factor, minm_no_of_neighbours)
#print(faces)
for face in faces:
    # we can check the dimension of the detected face
    # print(face)

    # the detected face is represented in the form if a rectangle
    x, y, w, h = face
    # draw a rectangle on the face in the image
    cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 2) # (image, top_left_ corner, bottom_right_corner, color_of_rectangle, color_thickness)

# show the image
cv2.imshow("Detected Faces",img)
# hold the window
cv2.waitKey(0)
# destroy all windows
cv2.destroyAllWindows()

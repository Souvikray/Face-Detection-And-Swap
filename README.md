Face detection is the process of identifying faces in a given image.The basic process of face detection is composed of the following steps

1 Machine Learning Examples

2 Features

3 Adaboost

4 Cascade Of Classifiers

<b> Machine Learning Examples </b>

Initially we train our machines with lots and lots of examples consisting of positive and negative images.Positive images refers to images with faces while negative images refers to images with no faces.

<b> Features </b>

It is quantifiable properties shared by image examples.So an image will have hundered of thousands of features.For eg a person's eye area,his/her lip area etc and so on.So we call these features as Haar features.It is of following types

Edge features

Line features

Four rectangle features

For eg the Edge features can be used to say detect the person's eye area which happens to be darker than say the person's nose area.So using the above features we can detect face areas in an image.But these features can vary from thousands to hundereds of thousands which can become time consuming if we were to compare each of the feature with the given window on the image at a time.So we look for some optimization to reduce the no of features to check.

<b> Adaboost </b>

It is basically feature selection.So we select the best features that defines the face area from the hundreds of thousands of features.So now we bring down the no of features to a few thousands.This is a great imporovement!But again checking the image with these thousands of features will be time consuming and inefficient.So we need to do something more.

<b> Cascade Of Classifiers </b>

Here the idea is that in an image most of the regions are non face region.So we can come up with a simple method to check whether a window (the current set of points in the image) is a non face region.If it is, then discard it and don't process it again.Move to the next region.So the idea of Cascade of Classifiers is instead of applying all the features to a window, group the features into different stages of classifiers.If a window fails the first stage, it is discarded.We don't move further.If the window passes the stage, then it moves to the next stage and so on.The window which cleras all the stage is a face region.

There are two important parameters that we need to pass when we check for a face in an image.

1 Scale factor

2 Minimum number of neighbours

<b> Scale factor </b>

It is basically a measure of by how much should we shrink our image at each level.If the image is too big, it is difficult for the face detection algorithm to detect faces.So we scale down the image by some constant percentage at each level such that it is either detected by the algorithm or there is no face at all.Our image must be robust to size variance.So whether we have a selfie or a family photo, the face detection algorithm must be able to work just fine.

<b> Minimum no of neighbours </b>

It is the number of neigbours that a candidate face needs to retain it.Usually when we detect faces in an image, many a times we end getting false positive(detection of a face in a region when there is no face in that region).So to reduce this,we use this parameter.If a region really does have a face and it is detected by the algorithm, then even though we shrink the image, we must still be able to detect the same face since we are not changing the image just shrinking the size.So this process will create multiple detection in the same area and the more no of detections, the more confident we are that it must be a face.However if it is a false positive, the algorithm may have made a mistake once but it won't make again so subsequent shrinking of the image won't result in detection of false positive in the same area again and again.So the higher we have Minimum number of neighbours, the more confident we are that it must be a face.

Now let us have a look at the Face Detection algorithm in action.

Original Image
![Alt text](https://github.com/Souvikray/Face-Detection-And-Swap/blob/master/mypic3.png?raw=true "Optional Title")

Face Detected
![Alt text](https://github.com/Souvikray/Face-Detection-And-Swap/blob/master/Screenshot1.png?raw=true "Optional Title")

Face and Eyes both detected
![Alt text](https://github.com/Souvikray/Face-Detection-And-Swap/blob/master/Screenshot2.png?raw=true "Optional Title")

Now let's have some fun.I will take an image which contains two individuals and detect the two faces and swap them.The idea is if I get coordinates of the two detected faces and adjust their sizes such that they have equal size, then I can just swap the coordinates and create hillarious picture. 

Original Image (That's me and my pal)
![Alt text](https://github.com/Souvikray/Face-Detection-And-Swap/blob/master/mypic4.jpg?raw=true "Optional Title")

After face swap
![Alt text](https://github.com/Souvikray/Face-Detection-And-Swap/blob/master/Screenshot3.png?raw=true "Optional Title")

I can similarly get the coordinates of the respective eyes, resize them and swap the coordinates.

After eyes swap
![Alt text](https://github.com/Souvikray/Face-Detection-And-Swap/blob/master/Screenshot4.png?raw=true "Optional Title")

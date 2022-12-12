# *SHOT TYPE CLASIFFICATION FOR ADS*

## Industries: adtech, marketing, content production and distribution

A shot type is defined by how close the camera is to the subject or object that's being filmed or captured in an image. 

Classifying shot type is challenging due to the physical information required beyond the video or image, such as the spatial composition of a frame and camera movement. 

We use Machine Learning deep models (CNN, LSTM, CNN 3D) to solve this challenge.

This project is about classifying shot types from two main groups: 

#### (a) Shot Scale

#### (b) Shot Movement.



![Types of shots](https://github.com/DaDeCar/final-project-shot-type/blob/570b293e1670c551fed6d8db33600ad298e782ac/Final_report/images/types_of_Shots.jpg)




#### Inside Shot scale, we have five categories:

1. long shot (LS) is taken from a long distance, sometimes as far as a quarter of a mile away;

2. full shot (FS) barely includes the human body in full;

3. medium shot (MS) contains a figure from the knees or waist up;

4. close-up shot (CS) concentrates on a relatively small object, showing the face of the hand of a person;

5. extreme close-up shot (ECS) shows even smaller parts such as the image of an eye or a mouth.




#### In the case of Shot movement, we have four categories:

1. in the static shot, the camera is fixed but the subject is flexible to move;

2. for motion shot, the camera moves or rotates;

3. the camera zooms in for push shot

4. zooms out for pull shot.!



Finally, to solve the project we used two models:

 a. CNN 2D + RNN

 Reference: https://keras.io/examples/vision/video_classification/

 b. CNN 3D (2D+1) with residual connections

 Reference: https://www.tensorflow.org/tutorials/video/video_classification

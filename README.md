SHOT TYPE CLASIFFICATION FOR ADS

Industries: adtech, marketing, content production and distribution

A shot type is defined by how close the camera is to the subject or object that's being filmed or captured in an image. Classifying shot type is challenging due to the physical information required beyond the video or image, such as the spatial composition of a frame and camera movement. 

This project is about classifying shot types from two main groups: 
(a) Shot Scale, and 
(b) Shot Movement.



reference


Inside Shot scale, we have five categories:

long shot (LS) is taken from a long distance, sometimes as far as a quarter of a mile away;

full shot (FS) barely includes the human body in full;

medium shot (MS) contains a figure from the knees or waist up;

close-up shot (CS) concentrates on a relatively small object, showing the face of the hand of a person;

(5) extreme close-up shot (ECS) shows even smaller parts such as the image of an eye or a mouth.



In the case of Shot movement, we have four categories:

in the static shot, the camera is fixed but the subject is flexible to move;

for motion shot, the camera moves or rotates;

the camera zooms in for push shot, and

zooms out for pull shot.








To solve the project we used two models:

 a. CNN 2D + RNN

 Reference: https://keras.io/examples/vision/video_classification/

 b. CNN 3D (2D+1) with residual connections

 Reference: https://www.tensorflow.org/tutorials/video/video_classification
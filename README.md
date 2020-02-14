# Real-Time-Facial-Recognition-using-DLIB

Real time face recognition using deep learning libraries. I used Dlib and face recognition library. Combination of these are giving high accuracy. 

Just follow the few simple steps:

1. First create folder with name of user inside dataset folder and insert around 50 pictures of user's face in different angles. Refer to my dataset.

2. Then run "python encode_faces.py --dataset dataset --encodings encodings.pickle" in cmd. 

3. If you want real time recognition then run "python recognize_faces_video.py --encodings encodings.pickle" in cmd. 

It can be trainned using cnn or hog. If you are using cpu then go with hog otherwise cnn. In both the steps you can add "--detection-method hog" if you want to detect and train with hog. Though, it's default is cnn.


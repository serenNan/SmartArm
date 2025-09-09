### Prerequisites
To run the programs, you need to create a virtual environment:
If you are using conda:
- create an environment using the command:
 - `conda create -n NAME python=3.8`
- install all packages you need:
 - `pip install -r requirements.txt`

If you dont have conda:
- create a virtual environment using the command:
  - `python -m venv venv`
- activate the virtual environment
  - `cd ./venv/Scripts/activate` (windows users)
  - `source ./venv/bin/activate` (mac and linux users)
- install the requirements
  - `pip install --upgrade pip` (to upgrade pip)
  - `pip install -r requirements.txt`

Once the requirements have been installed, The programs will run successfully.

For vision:
```
Tensorflow>2
OpenCV
sklearn=0.19.1 # for face spoofing. 
The model used was trained with this version and does not support recent ones.
```


### Face detection
Earlier, Dlib's frontal face HOG detector was used to find faces. However, it did not give very good results. In [face_detection](../../tree/master/face_detection) different face detection models are compared and OpenCV's DNN module provides best result and the results are present in [this article](https://towardsdatascience.com/face-detection-models-which-to-use-and-why-d263e82c302c?source=friends_link&sk=c9e2807cf216115d7bb5a9b827bb26f8).

It is implemented in `face_detector.py` and is used for mouth opening detection and head pose estimation.

An additional quantized model is also added for face detector as described in [Issue 14](https://github.com/vardanagarwal/Proctoring-AI/issues/14). This can be used by setting the parameter `quantized` as True when calling the `get_face_detector()`. On quick testing of face detector on my laptop the normal version gave ~17.5 FPS while the quantized version gave ~19.5 FPS. This would be especially useful when deploying on edge devices due to it being uint8 quantized.

### Facial Landmarks
Earlier, Dlib's facial landmarks model was used but it did not give good results when face was at an angle. Now, a model provided in this [repository](https://github.com/yinguobing/cnn-facial-landmark) is used. A comparison between them and the reason for choosing the new Tensorflow based model is shown in this [article](https://towardsdatascience.com/robust-facial-landmarks-for-occluded-angled-faces-925e465cbf2e?source=friends_link&sk=505eb1101576227f4c38474092dd4c22).

It is implemented in `face_landmarks.py` and is used for mouth opening detection and head pose estimation.

### Mouth Opening Detection
`mouth_opening_detector.py` is used to check if the candidate opens his/her mouth during the exam after recording it initially. However, it is using dlib which can be easily changed to the new models.

![Mouth opening detection](../gifs/2.gif)

### Head pose estimation
`head_pose_estimation.py` is used for finding where the head is facing. An explanation is provided in this [article](https://towardsdatascience.com/real-time-head-pose-estimation-in-python-e52db1bc606a?source=friends_link&sk=0bae01db2759930197bfd33777c9eaf4)

![head pose estimation](../../blob/master/gifs/3.gif)

### FPS obtained

Functionality | On Intel i5
--- | ---
Eye Tracking | 7.1
Mouth Detection | 7.2
Head Pose Estimation | 8.5

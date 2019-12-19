# facenet_face_recogniton

dependencies:

 1) imutils
 2) pickle
 3) sklearn
 4) openCV >= 3.4
 5) python >= 2.7

download the pretarined facenet_model here: https://drive.google.com/file/d/1Ds6gqY9dNRlbYA61zpv2ejzKbcjnhb-2/view?usp=sharing

download the protobuf files for face_detection: https://drive.google.com/open?id=1bL8KmZZRIR6yEpWAA6QNQiNzKBLmKJsu

download the output directory to store emebddings: https://drive.google.com/open?id=1Ql5YlQ2X-Y1ssGm0Xs3DtWpXUbUmT_00

Create a 'dataset' directory with the structure (atleast 2 users are required):

 1) user1 - some (6-10) photos
 2) user2 - some " photos
 3) user3 - some " photos
 4) unknown - some random face images 
 
Instructions to run:

# this code extracts the embeddings given by face_net model:
1) python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7

# this code trains the images in the dataset folder on a SVM for classification:
2) python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle

# this is for testing with the webcam 
3) python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle

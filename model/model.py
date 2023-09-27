from deepface import DeepFace
import numpy as np
import cv2

bharath = './data_images/bharath/bharath_4.jpg'
kelmith = './data_images/faye/faye_3.jpg'
mix = './data_images/faye_reddy/faye_reddy_7.jpg'

img1 = cv2.imread(bharath)
img2 = cv2.imread(mix)

#Model to recognize
models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
]


#Face detectors
backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
]


#distance metics
metrics = ["cosine", "euclidean", "euclidean_l2"]

faces = DeepFace.extract_faces(img_path=mix, target_size=(224,224),detector_backend=backends[4])


for detected_faces in faces:
    name = "found" + str(detected_faces["confidence"])
    
    
    dfs = DeepFace.find(img_path=detected_faces['face'],db_path='data_images')
    print(dfs)
    
    
    cv2.imshow(name,detected_faces['face'])
cv2.waitKey(0)

# for i,face in detected_faces:
#     print(face['face'])
    # name = f'faces_{i}'
    # cv2.imshow(name,face['face'])
    # #cv2.imshow(name,np.array(face,dtype='uint8'))
    # cv2.waitKey(0)

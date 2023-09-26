from deepface import DeepFace
import cv2

img_1 = '../api/temp/11.jpg'
img_2 = '../api/temp/14.jpg'

img1 = cv2.imread(img_1)
img2 = cv2.imread(img_2)


results = DeepFace.verify(img1_path=img1, img2_path=img2)

print(results)

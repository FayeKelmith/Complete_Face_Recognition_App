from retinaface import RetinaFace
import matplotlib.pyplot as plt
resp = RetinaFace.extract_faces("../model/data_images/faye_reddy/faye_reddy_8.jpg", align= False)

for face in resp:
    plt.imshow(face)
    plt.show()


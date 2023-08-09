# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import cv2
import os


# ---------------------------------------------------------------------------- #
#                                   Constants                                  #
# ---------------------------------------------------------------------------- #
FLOWERS = ['daisy','dandelion','rose','sunflower','tulip']



# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #

flower_data = []
for flower_type in FLOWERS:
    flower_images = os.listdir('Flower_data/flowers/' + flower_type +'/')

    list_hist = []
    for flower in flower_images:
        
        img = cv2.imread('Flower_data/flowers/' + flower_type +'/' + flower)
        img = cv2.resize(img, (150,150))

        list_hist.append(cv2.calcHist([img], [0,1,2],None, [6,6,6], [0,256,0,256,0,256]))

    flower_data.append(list_hist)

print(list_hist)
#print("3D histogram shape: {}, with {} values".format(
#	hist.shape, hist.flatten().shape[0]))
# display the original input image


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
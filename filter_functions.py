import cv2
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np

# Module with functions for filtering images 

def averaging_filter(image_list, n):
    """Perform averaging filtering of images with a nxn mask"""
    smooth_images = []
    for image in image_list:
        size = (image.shape[0] - (n//2)*2, image.shape[1] - (n//2)*2)
        smooth_image = np.zeros(size)
        for i in range(n//2, image.shape[0] - n//2):
            for j in range(n//2, image.shape[1] - n//2):
                suma = 0
                for ii in range(i-n//2, i+n//2+1):
                    for jj in range(j-n//2, j+n//2+1):
                        suma += image[ii][jj]
                smooth_image[i-n//2][j-n//2] = round(suma/(n*n))
        smooth_images.append(smooth_image)
    return smooth_images
import cv2
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
from cmath import pi

# Module with functions for filtering images 

def averaging_filter(image_list, n):
    """
    Perform averaging filtering of images with a nxn size mask
    The function returns a list of smoothed images
    """
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

def gauss_mask(n,sigma):
    s = (n,n)
    D = np.ones(s)
    sumawag = 0
    for i in range(n):
        for j in range(n):
            D[i][j]=np.sqrt((i-(n//2))**2+(j-(n//2))**2)
    G = np.zeros_like(D)
    for i in range(0,n):
        for j in range(0,n):
            G[i][j]=1/(2*pi*sigma**2)*np.exp(-D[i][j]**2/(2*sigma**2))
            sumawag+=G[i][j]
    return G,sumawag

def gauss_filter(n,sigma,image_list):
    gauss_images = []
    for image in image_list:
        size = (image.shape[0] - (n//2)*2, image.shape[1] - (n//2)*2)
        newimage = np.ones(size)
        G,sumawag = gauss_mask(n,sigma)
        for i in range(0,size[0]):
            for j in range(0,size[1]):
                suma=0
                di = 0
                for ii in range(i,i+n):
                    dj=0
                    for jj in range(j,j+n):
                        suma+=image[ii][jj]*G[di][dj]
                        dj+=1
                    di+=1
                newimage[i][j] = round(suma/sumawag)   
        gauss_images.append(newimage)
    return gauss_images

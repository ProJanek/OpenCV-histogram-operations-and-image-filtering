"""Module with functions for filtering images."""

import numpy as np
from cmath import pi

def averaging_filter(n, image_list):
    """
    Perform averaging filtering of images with a nxn size mask.
    The function returns a list of smoothed images.
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
    """Create a gauss filter for a given size and sigma."""
    s = (n,n)
    # D - distances from the center point of the mask
    D = np.ones(s)
    sum = 0
    for i in range(n):
        for j in range(n):
            D[i][j]=np.sqrt((i-(n//2))**2+(j-(n//2))**2)
    # G - gauss filter mask 
    G = np.zeros_like(D)
    for i in range(n):
        for j in range(n):
            G[i][j]=1/(2*pi*sigma**2)*np.exp(-D[i][j]**2/(2*sigma**2))
            sum+=G[i][j]
    return G,sum

def gauss_filter(n,sigma,image_list):
    """
    Perform gauss filtering of images with a nxn size mask.
    The function returns a list of smoothed images.
    """
    gauss_images = []
    for image in image_list:
        size = (image.shape[0] - (n//2)*2, image.shape[1] - (n//2)*2)
        gauss_image = np.zeros(size)
        G,sum = gauss_mask(n,sigma)
        for i in range(n//2, image.shape[0] - n//2):
            for j in range(n//2, image.shape[1] - n//2):
                suma=0
                di = 0
                for ii in range(i-n//2, i+n//2+1):
                    dj=0
                    for jj in range(j-n//2, j+n//2+1):
                        suma+=image[ii][jj]*G[di][dj]
                        dj+=1
                    di+=1
                gauss_image[i-n//2][j-n//2] = round(suma/sum)   
        gauss_images.append(gauss_image)
    return gauss_images

def median_filter(n, image_list):
    """
    Perform median filtering of images with a nxn size mask.
    The function returns a list of smoothed images.
    """
    median_images = []
    for image in image_list:
        size = (image.shape[0] - (n//2)*2, image.shape[1] - (n//2)*2)
        median_image = np.zeros(size)
        for i in range(n//2, image.shape[0] - n//2):
            for j in range(n//2, image.shape[1] - n//2):
                pixels = []
                for ii in range(i-n//2, i+n//2+1):
                    for jj in range(j-n//2, j+n//2+1):
                        pixels.append(image[ii][jj])
                # sort pixels collection 
                pixels.sort()
                middle = int((len(pixels)-1)/2)
                # sssign a median 
                median_image[i-n//2][j-n//2] = pixels[middle]
                del pixels[:]   
        median_images.append(median_image)
    return median_images
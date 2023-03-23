import cv2
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np

# Module with functions working on histogram 

def create_image_path_list(path):
    """Create a list of paths to images in a directory"""
    images = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    return images

def convert_to_grey_scale(image_path_list):
    """Load the images, convert images to grey scale and keep them in list"""
    grey_images = []
    for image_path in image_path_list:
        image_temp = cv2.imread(image_path)
        image_grey = cv2.cvtColor(image_temp, cv2.COLOR_BGR2GRAY)
        grey_images.append(image_grey)
    return grey_images

def histogram_stretch(image_list):
    """Stretch the histogram for the images in the list and keep them in the list"""
    hist_str_images = []
    for image in image_list:
        f_max = 0
        f_min = 255
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i][j] > f_max:
                    f_max = image[i][j]
                if image[i][j] < f_min:
                    f_min = image[i][j]
        hist_str_image = image
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                hist_str_image[i][j] = (
                    image[i][j] - f_min)/(f_max - f_min)*f_max
        hist_str_images.append(hist_str_image)
    return hist_str_images

def histogram_equalization(image_list):
    """Equalize the histogram for the images in the list and keep them in the list"""
    hist_equal_images = []
    for image in image_list:
        histogram = np.zeros(256, dtype=int)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                histogram[image[i][j]] += 1
        # p - probability of a given level of gray
        p = np.zeros(256)
        for i in range(len(p)):
            p[i] = histogram[i]/(image.shape[0]*image.shape[1])
        # d - distribution function for p
        d = np.zeros(256)
        d[0] = p[0]
        for i in range(1,len(d)):
            d[i] = d[i-1] + p[i]
        # y - value obtained from an equal histogram
        y = np.zeros(256)
        for i in range(len(y)):
            y[i] = round((d[i] - min(d))/(1-min(d))*(256-1))
        temp_image = np.zeros_like(image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                temp_image[i][j] = y[image[i][j]]
        hist_equal_images.append(temp_image)           
    return hist_equal_images

def save_histogram(image, filename):
    """Save histogram for one image"""
    histogram = np.zeros(256, dtype=int)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i][j]] += 1
    ax = plt.subplot(111)
    ax.bar(list(range(256)), histogram, color='g',)
    plt.savefig(filename)

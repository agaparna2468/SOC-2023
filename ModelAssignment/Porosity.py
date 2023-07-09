import cv2
import numpy as np
import math

img = cv2.imread('Sample Image.jpg', cv2.IMREAD_GRAYSCALE)      #Reading the image in Grayscale

retval, img_thresh = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)   # Values above 60 are given 255 which is white and values below 60 are given 0 which is black

x, y = img_thresh.shape
total_no = x*y          # Total number of pixels
pores = total_no - np.count_nonzero(img_thresh == 255)      # Number of pixels considered as black
# print(np.count_nonzero(img_thresh == 255))
# print(total_no)
# print(pores)
print(f'Porosity calculated using binary thresholding with intensities below 60 are given 0: {math.ceil((pores/total_no)*10000)/100}')

img_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 7)   # The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant 7

x, y = img_thresh.shape
total_no = x*y
pores = total_no - np.count_nonzero(img_thresh == 255)      # Number of pixels considered as black
#print(np.count_nonzero(img_thresh == 255))
#print(total_no)
#print(pores)
print(f'Porosity calculated using binary thresholding with the threshold value is a gaussian-weighted sum of the neighbourhood values in block size 11 minus the constant 7: {math.ceil((pores/total_no)*10000)/100}')
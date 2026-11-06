# pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')

if img is None:
    print("Error: Could not load image.")
    exit()

cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print("Original:", img.shape)
print("Blue:", b.shape)
print("Green:", g.shape)
print("Red:", r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
cv.destroyAllWindows()
## Importing Libraries
import numpy
import cv2

## Taking Input Image
img = cv2.imread('pots.jpg')

# Splitting into separate channels
b,g,r = cv2.split(img)

# Display the images
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

# Save the images
cv2.imwrite('b.jpg', b)
cv2.imwrite('g.jpg', g)
cv2.imwrite('r.jpg', r)

## END OF FILE
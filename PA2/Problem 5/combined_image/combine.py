## Importing Libraries
import numpy
import cv2

## Loading Images
r = numpy.load('x_r.npy')
g = numpy.load('x_g.npy')
b = numpy.load('x_b.npy')

## Merging Images
image = cv2.merge((b,g,r))

# Displaying the image
cv2.imshow('combined', image)

# Saving the final image
cv2.imwrite("final_image.jpg",image)

## END OF FILE
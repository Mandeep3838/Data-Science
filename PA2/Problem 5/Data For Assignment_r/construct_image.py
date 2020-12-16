## Importing Libraries
import numpy
import cv2

## Loading arrays
A_inv = numpy.load('A_inv.npy')
s = numpy.load('s_r.npy')

# Computing A_inv*s to get image
image = numpy.matmul(A_inv, s)

# Normalizing values to (0,1)
image = (image - min(image))/(max(image)-min(image))
image = image.reshape(100,100).T

# Scaling image to (0,255)
image *= 255.0

# Saving image
numpy.save('x_r', image)

## END OF FILE
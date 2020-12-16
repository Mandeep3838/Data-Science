## Importing Libraries
import numpy
import cv2

## Loading arrays
A_inv = numpy.load('A_inv.npy')
s = numpy.load('s_g.npy')

## Computing A_inv*s
image = numpy.matmul(A_inv, s)

# Normalizing values to (0,1)
image = (image - min(image))/(max(image)-min(image))
image = image.reshape(100,100).T

# Scaling values to (0,255)
image *= 255.0

# Save the computed image
numpy.save('x_g', image)

## END OF FILE
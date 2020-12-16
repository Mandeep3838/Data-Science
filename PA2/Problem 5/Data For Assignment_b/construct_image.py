## Importing Libraries
import numpy
import cv2

## Importing arrays
A_inv = numpy.load('A_inv.npy')
s = numpy.load('s_b.npy')

## Compute A_inv*s to get the image
image = numpy.matmul(A_inv, s)

# Normalize the values to (0,1)
image = (image - min(image))/(max(image)-min(image))
image = image.reshape(100,100).T

# Scale the values to (0,255)
image *= 255.0

# Save the computed image
numpy.save('x_b',image)

## END OF FILE
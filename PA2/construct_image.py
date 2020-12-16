
## Importing Librariess
import numpy
import cv2

## Loading Arrays
A_inv = numpy.load('A_inv.npy')
s = numpy.load('st.npy')

## Computing A_inv*s to get x
image = numpy.matmul(A_inv, s)

# Normalize x to get all values in (0,1)
image = (image - min(image))/(max(image)-min(image))

# Taking Transpose of Reshaped x to get desired image
image = image.reshape(100,100).T

# Scale all values to range (0,255)
image *= 255.0

# Save the Reconstructed Image
cv2.imwrite('reconstructed_image.jpg', image)

## END OF FILE
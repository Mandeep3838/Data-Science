# Importing Libraries
import glob
import numpy
import sys
from PIL import Image
from scipy.linalg import svd

import matplotlib.pyplot as plt

''' Function for compressing image data
    1. Input <- Images, k(principal components)
    2. Centering the data and finding covariance matrix
    3. singular value decomposition of covariance matrix
    4. Keeping first i eigen vectors (By default eigen vectors are sorted according to highest eigen values)
    5. Projecting data on selected eigen vectors
'''
def compress(images,i):
    mean = images.mean(axis=0)
    cen_images = images - mean
    cov_matrix = numpy.cov(cen_images.T, bias=True)
    U, s, VT = svd(cov_matrix)
    U = numpy.delete(U, numpy.s_[i:], axis=1)
    reduced_img = numpy.matmul(cen_images, U)
    return mean, U, reduced_img

''' Function to Reconstruct Images
    1. Input <- Reduced Images, k eigen vectors, mean
    2. Reconstructing images from reduced presentation

'''
def decompress(reduced_img, U, mean):
    reconstuct_images = numpy.matmul(reduced_img, U.T) + mean
    return reconstuct_images


org_images = []

# Take input from user 
p_value = int(input("Enter Components required (1-4096):"))

# Plotting original images
fig = plt.figure(figsize=(8,8))
col = 6
row = 5
i=1

for img in glob.glob("./Mandeep Bawa and ANUBOLA SAI ABHINAY/*.png"):
    image = Image.open(img)
    org_images.append(numpy.asarray(image))
    fig.add_subplot(row, col, i)
    plt.axis('off')
    plt.imshow(image)
    i+=1
fig.suptitle("Original Images")

# Taking images and reshaping it to (n_samples, 4096) 
org_images = numpy.array(org_images)
org_images = org_images.reshape(-1,64*64)

# Compressing the images
mean, U, reduced_img = compress(org_images, p_value)

print("Shape of reduced image: {shape}".format(shape=reduced_img.shape))

# Decompressing and reshaping to (n_samples, 64, 64)
decom_images = decompress(reduced_img, U, mean)
decom_images = decom_images.reshape(-1,64,64)

# Plotting images after reconstructing 
fig2 = plt.figure(figsize=(8,8))
col = 6
row = 5
i=1

for i in range(decom_images.shape[0]):
    fig2.add_subplot(row, col, i+1)
    plt.axis('off')
    plt.imshow(decom_images[i])
    i+=1

fig2.suptitle("Decompressed Images")

plt.show()

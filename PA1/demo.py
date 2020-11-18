import glob
import numpy
import sys
from PIL import Image
from scipy.linalg import svd

import matplotlib.pyplot as plt

def compress(images,i):
    W = []
    compressed_images = []
    for image in images:
        cov_matrix = numpy.cov(image, bias=True)
        U, s, VT = svd(cov_matrix)
        U = numpy.delete(U, numpy.s_[i:], axis=1)
        reduced_mat = numpy.matmul(U.T, image)
        compressed_images.append(reduced_mat)
        W.append(U)
    return compressed_images, W

def decompress(com_images, W):
    decom_images = []
    for i in range(len(com_images)):
        com_image = com_images[i]
        wei = W[i]
        regen_image = numpy.matmul(wei, com_image)
        decom_images.append(regen_image)
    return decom_images

org_images = []
p_value = int(input("Enter Components required:"))

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
# plt.show()

for i in range(len(org_images)):
    print("Origninal Image {index}: {shape}".format(index=i, shape=org_images[i].shape))

com_images, W = compress(org_images, p_value)

for i in range(len(org_images)):
    print("Compressed Image {index}: {shape}".format(index=i, shape=com_images[i].shape))

decom_images = decompress(com_images, W)

fig2 = plt.figure(figsize=(8,8))
col = 6
row = 5
i=1

for img in decom_images:
    fig2.add_subplot(row, col, i)
    plt.axis('off')
    plt.imshow(img)
    i+=1
fig2.suptitle("Decompressed Images")
plt.show()


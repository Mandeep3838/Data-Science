
import numpy
import pandas
import glob

from PIL import Image
from scipy.linalg import svd

img = Image.open('0.png')

for img in glob.glob("./Mandeep Bawa and ANUBOLA SAI ABHINAY/"):
    print(img)


data = numpy.asarray(img)
cov_matrix = numpy.cov(data, bias=True)

U, s, VT = svd(data)

# print(U)
print(s[:5])
# print(VT)

# reconstruct image matrix
reduced_values = numpy.zeros((s.shape[0]))
reduced_values[:3] = s[:3]
sigma = numpy.diag(reduced_values)
# print(sigma)

A_C = numpy.matmul(U, numpy.matmul(sigma, VT))
print(A_C)

recon_img = Image.fromarray(A_C)
recon_img.show()




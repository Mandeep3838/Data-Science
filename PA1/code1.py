
import numpy
import pandas

from PIL import Image
from scipy.linalg import svd

img = Image.open('0.png')

data = numpy.asarray(img)
print("Data values: {}".format(data))
# sub mean from columns
# mean_sub = data - numpy.mean(data, axis=1)
cov_matrix = numpy.cov(data, bias=True)

U, s, VT = svd(cov_matrix)

U = numpy.delete(U, numpy.s_[20:], axis=1)

reduced_mat = numpy.matmul(U.T, data)
recons_mat = numpy.matmul(U, reduced_mat)
print("Reconstructed values {}".format(recons_mat))
recon_img = Image.fromarray(recons_mat)
recon_img.show()




import numpy

def mod_derivate(s):
    derv = []
    for i in range(s.shape[0]):
        if s[i] > 0:
            derv.append(1)
        elif s[i] < 0:
            derv.append(-1)
        else:
            derv.append(0)
    derv = numpy.array(derv)
    derv = derv.reshape(-1,1)
    return derv

def lagrange_derv_s(C, s, v):
    return mod_derivate(s) - numpy.matmul(C.T, v) 


C = numpy.load('C.npy')

s = numpy.load('st.npy')

y= numpy.load('y.npy')

nu = numpy.load('nu.npy')

print(numpy.linalg.norm(numpy.matmul(C,s)-y,2))


## Verify derivate w.r.t s

print(numpy.linalg.norm(lagrange_derv_s(C, s, nu)))


import numpy as np

print("Check whether f(x) = (x.T).A.x is convex or not for x taking integer values")
print("Check whether f(tx+(1-t)y) <= tf(x) + (1-t)f(y)")

def f(A,x):
    return np.matmul(np.matmul(x.T,A),x)

def isconvex(A,x,y,t):
    lhs = f(A,t*x+(1-t)*y)
    rhs = t*f(A,x) + (1-t)*f(A,y)
    return lhs <= rhs



A = np.array([[1,0],[2,1]])

print(A)
i=0

while(True):
    x = np.random.randint(-10,10,2)
    y = np.random.randint(-10,10,2)
    t = np.random.uniform(0,1)
    if not isconvex(A,x,y,t):
        i+=1
        print("Contradict example " +str(i) +  " : A =" + str(A.tolist()) + " x =" + str(x) + "\ty =" + str(y) + "\tt =" + str(t))
    if i>=11:
        break
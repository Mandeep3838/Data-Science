
## Imporing Libraries
import numpy
import cvxpy as cp

## Taking Input
# Loading y and C from the files provided
y = numpy.load('y.npy')
C = numpy.load('C.npy')

# Random Seed
numpy.random.seed(1)

## Construct the Convex Optimisation problem
# Problem Initialization
s = cp.Variable((C.shape[1],1))
objective = cp.Minimize(cp.norm(s,1))
constraints = [y==C@s]

# Problem Setup
prob = cp.Problem(objective, constraints)

# Solving the Convex problem
result = prob.solve()

## Saving to Directory
# Save s* 
ls = []
for i in range(10000):
  ls.append(s[i].value)

x = numpy.array(ls)
x = x.reshape(-1,1)
numpy.save('s',x)

# Save nu* 
ls = []
for i in range(3000):
  ls.append(prob.constraints[0].dual_value[i])

nu = numpy.array(ls)
nu = nu.reshape(-1,1)
numpy.save('nu',nu)

## END OF FILE
from cvxopt import *
from numpy import *
m = 30
n = 100
Are = randn(m,n) 
Aim = randn(m,n)
bre = randn(m,1)
bim = randn(m,1)
A = Are + 1j*Aim
b = bre + 1j*bim

Atot1 = hstack([Are, -Aim])
Atot2 = hstack([Aim, Are])
Atot = matrix(vstack([Atot1, Atot2]))
btot = matrix(vstack([bre, bim]))
z_2 = Atot.T*inv(Atot*Atot.T)*btot
x2 = z_2[0:99]+1j*z_2[100:199]
print x2

#cvxpy
from cvxpy import Variable, norm2, Problem, Minimize
x = Variable (2*n,1)
objective = Minimize(norm2(x))
constraints = [Atot*x == btot]
pro = Problem(objective, constraints) 
result = pro.solve()
xnorm = x.value[0:99]+1j*x.value[100:199]
print x2-xnorm
#cvxpy norminf
from cvxpy import normInf,norm1
xinf = Variable (2*n,1)
objective1 = Minimize(normInf(xinf))
constraints1 = [Atot*xinf == btot]
pro1 = Problem(objective1, constraints1) 
result = pro1.solve()
#print xinf.value[0:99]+1j*xinf.value[100:199]
scatter(x.value[0:99],x.value[100:199])
scatter(xinf.value[0:99],xinf.value[100:199],c='r',marker='D')

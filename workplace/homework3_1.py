from cvxpy import *
from cvxopt import matrix

A = matrix([[1,0,0,2,1],[2,0,3,1,0],[0,3,1,2,3],[1,1,1,5,2]])
cmax = matrix([100,100,100,100,100])
p = matrix([3.0,2.0,7.0,6.0])
pdisc = matrix([2,1,4,2])
q = matrix([4,10,5,10])
u = Variable(4,1)
x = Variable(4,1)
#qq = [min(p[i]*x[i], p[i]*q[i] + pdisc[i]*(x[i]-q[i])) for i in range(x.size[0])]
objective = Maximize(sum(u))
constraints1 = [0 <= x, A*x <= cmax]
constraints2 = [(p[i]*x[i]>=u[i]) for i in range(x.size[0])]
constraints3 = [((p[i]*q[i]+pdisc[i]*(x[i]-q[i]))>=u[i]) for i in range(x.size[0])] 
constraints = constraints1+constraints2+constraints3
pro = Problem(objective, constraints)
result = pro.solve()
print x.value
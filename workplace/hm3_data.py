from scipy import linalg, matrix
def nullspace(A, atol=1e-13, rtol=0):
     A = np.atleast_2d(A)
     u, s, vh = svd(A)
     tol = max(atol, rtol * s[0])
     nnz = (s >= tol).sum()
     ns = vh[nnz:].conj().T
     return ns




a1= matrix(linspace(0,1,10))
a2 = matrix([1.9, 1.8, 1.0, 1.1, 1.9, 1.8, 1.9, 1.7, 1.5, 1.5])
L=vstack([a1,a2])
m=L.shape[1]
V11 = [0.0, 0.1, 0.15, 0.2, 0.1, 0.2, 0.3, 0.0, 0.0, 0.0,0.1, 0.2, 
      0.2, 0.0, 0.1, 0.05, 0.1, 0.1, 0.0, 0.2, 0.1]
V2 = matrix(map(lambda x: x*0.4,V11))
V1 = matrix(linspace(0,1,21))
V = vstack([V1,V2])
n = V.shape[1]
plot(array(a1.T),array(a2.T),'o',array(V1.T),array(V2.T),"-")

dV = V[:,1:n]-V[:,0:n-1]
VI=V[:,0:n-1]+0.5*dV
A=zeros((n,m))
for i in range(n-1):
    for j in range(m):
        dVI=L[:,j]-VI[:,i]
        dVperp = nullspace(dV[:,i].T)
        if dVperp[1]<0:
            dVperp=-dVperp
        A[i,j]=max(0,dVI.T*dVperp/(norm(dVI)*norm(dVperp)))

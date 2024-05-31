def Warshall(A):
    [L,C]=A.shape
    P=A.copy()
    for k in range(0,L):
        for i in range(0,L):
            for j in range(0,C):
                if P[i,j]==0:
                    P[i,j]=P[i,k] & P[k,j]
    return P

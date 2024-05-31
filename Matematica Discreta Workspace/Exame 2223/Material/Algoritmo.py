import numpy as np

def Warshall_Min(W):
    [a,b]=np.shape(W)
    
    Q=W.astype(float)
    
    M=np.empty((a, b))
    M=M.astype(str)
    for i in range(0,a):
        for j in range(0,a):
            if W[i,j]==0:
                Q[i,j]=np.inf
                M[i,j]='-'
            else:
                M[i,j]=str(i+1)+str(j+1)                
    print(M)
              
    for k in range(0,a):
        for i in range(0,a):
            for j in range(0,a):
                if Q[i,j]>Q[i,k]+Q[k,j]:
                    Q[i,j]=Q[i,k]+Q[k,j]
                    M[i,j]=M[i,k]+M[k,j][1:len(M[k,j])]     
    print(Q)
    print(M)
    
    S=[Q,M]
    return S
    


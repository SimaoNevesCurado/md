import numpy as np



def funcao1(M):
    [c,d]=M.shape
    Mi=M@M
    Br=M+Mi
    Br[Br!=0]=1
    return (M==Br).all()

def funcao2(M):
    [L,C]=M.shape
    A=M
    for i in range(2,L+1):
        A=A+np.linalg.matrix_power(M,i)
    A[A!=0]=1
    return A

def funcao3(MR):
    [c,d]=MR.shape
    for i in range(0,c):
        for j in range(i+1,d):
            if MR[i,j]!=MR[j,i]:
                return False
    return True


def funcao4(M):
    [L,C]=M.shape
    M=M+np.eye(L,L)
    M[M!=0]=1
    return M



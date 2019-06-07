import scipy
import scipy.sparse as sparse
import scipy.sparse.linalg
def eigsReal(L, M, k):
    """
    EIGSREAL computes generalized eigendecomposition 

    Inputs:
      L (|V|,|V|) matrix
      M (|V|,|V|) diagonal mass matrix
      k number of eigenvalues/eigenvectors to return
    Output:
      eVal (k,) eigenvalues
      eVec (|V|,k) eigenvectors
    """
    eVal, eVec = scipy.sparse.linalg.eigsh(L, M=M, k=k, which='LM', sigma = 0)
    return eVal, eVec
import numpy as np
import scipy
import scipy.sparse 
from cotmatrix import cotmatrix
from massmatrix import massmatrix

def meanCurvatureNormals(V, F):
    """
    MEANCURVATURENORMAL computes the mean curvature normal 

    Input:
        V (|V|,3) numpy array of vertex positions
        F (|F|,3) numpy array of face indices
    Output:
        HN (|V|,3) numpy array of mean curvature normal vector
    """
    L = cotmatrix(V,F)
    M = massmatrix(V,F,'voronoi')
    invM = scipy.sparse.diags(np.power(M.diagonal(),-1)).tocsr()
    HN = invM * (L * V)
    return HN    
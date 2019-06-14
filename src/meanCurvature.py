import numpy as np
import scipy
import scipy.sparse 
from meanCurvatureNormals import meanCurvatureNormals

def meanCurvature(V, F):
    """
    MEANCURVATURE computes the mean curvature normal 

    Input:
        V (|V|,3) numpy array of vertex positions
        F (|F|,3) numpy array of face indices
    Output:
        HN (|V|,3) numpy array of mean curvature normal vector
    """
    HN = meanCurvatureNormals(V,F)
    H = 0.5*np.sqrt(np.sum(HN**2,1))
    return H
    
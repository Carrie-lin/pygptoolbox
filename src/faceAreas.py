import numpy as np
import scipy
import scipy.sparse 

def faceAreas(V, F):
    """
    FACEAREAS computes area per face 

    Input:
        V (|V|,3) numpy array of vertex positions
        F (|F|,3) numpy array of face indices
    Output:
        FA (|F|,) numpy array of face area
    """
    # faceArea = np.zeros((F.shape[0],))
    # for ii in range(3):
    # 	idx1 = ii
    # 	idx2 = (ii+1)%3

    # 	Vtmp = V[:, [idx1, idx2]]
    # 	r = Vtmp[F[:,0],:] - Vtmp[F[:,2],:]
    # 	s = Vtmp[F[:,1],:] - Vtmp[F[:,2],:]
    # 	doubleArea = r[:,0] * s[:,1] - r[:,1] * s[:,0]
    # 	faceArea += np.power(doubleArea,2)
    # faceArea = np.sqrt(faceArea)/2
    vec1 = V[F[:,1],:] - V[F[:,0],:]
    vec2 = V[F[:,2],:] - V[F[:,0],:]
    FN = np.cross(vec1, vec2) / 2
    FA = np.sqrt(np.sum(FN**2,1))
    return FA
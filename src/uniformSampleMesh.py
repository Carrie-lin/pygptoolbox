import numpy as np
from faceAreas import faceAreas

def uniformSampleMesh(V, F, nPt):
    """
    UNIFORMSAMPLEMESH uniformly samples nPt points on a triangle mesh

    Input:
        V (|V|,3) numpy array of vertex positions
        F (|F|,3) numpy array of face indices
        nPt number of points to sample
    Output:
        P (nPt,3) numpy array of sampled point positions
    """
    FA = faceAreas(V,F)
    FASum = np.cumsum(FA)
    FASum /= FASum[-1]

    FIdx = np.random.rand(nPt,1)
    FIdx = np.searchsorted(FASum,FIdx).flatten()

    bary = np.random.rand(nPt, 3)
    bary = bary / np.sum(bary,axis=1)[:,None]

    P = bary[:,0:1]*V[F[FIdx,0],:] + bary[:,1:2]*V[F[FIdx,1],:] + bary[:,2:3]*V[F[FIdx,2],:]
    return P
import numpy as np

def normalizeUnitSphere(V):
    '''
    NORMALIZEUNITSPHERE normalize a shape to the bounding box with radius 1 and centered at the origin

    Inputs:
        V (|V|,3) numpy array of vertex positions

    Outputs:
        V |V|-by-3 numpy array of normalized vertex positions
    '''
    V = V - np.mean(V, axis = 0)
    V = V / np.max(V)
    return V
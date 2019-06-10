import numpy as np

def normalizeUnitCube(V):
    '''
    NORMALIZEUNITCUBE normalize a shape to the bounding box by 0.5,0.5,0.5

    Inputs:
        V (|V|,3) numpy array of vertex positions

    Outputs:
        V |V|-by-3 numpy array of normalized vertex positions
    '''
    V = V - np.min(V, axis = 0)
    V = V / np.max(V) / 2.0
    return V

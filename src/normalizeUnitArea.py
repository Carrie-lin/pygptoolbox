import numpy as np
from faceAreas import faceAreas

def normalizeUnitArea(V,F):
    '''
    NORMALIZEUNITAREA normalize a shape to have total surface area 1

    Inputs:
        V (|V|,3) numpy array of vertex positions
        F (|F|,3) numpy array of face indices

    Outputs:
        V |V|-by-3 numpy array of normalized vertex positions
    '''
    totalArea = np.sum(faceAreas(V,F))
    V = V / np.sqrt(totalArea)
    return V

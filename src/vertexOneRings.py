import numpy as np
from edges import *

def vertexOneRings(F):
	'''
    VERTEXONERINGS computs one ring vertices of each vertex of a triangle mesh
    
    Inputs:
    F: |F|-by-3 numpy ndarray of face indices
    
    Outputs:
    oneRing: list of list of vertex one ring indices
    '''
	E = edges(F)
	keys = np.array([])
	values = np.array([])
	keys = np.append(keys, E[:,0])
	keys = np.append(keys, E[:,1])
	values = np.append(values, E[:,1])
	values = np.append(values, E[:,0])

	faceDict = {}
	keys = keys.astype(int)
	values = values.astype(int)
	for ii in range(keys.shape[0]):
	    faceDict.setdefault(keys[ii],[]).append(values[ii])
	return faceDict.values() # return type is a list of list
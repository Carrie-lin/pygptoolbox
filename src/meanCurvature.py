import numpy as np 
from cotmatrix import *
from vertexAreas import *

def meanCurvature(V,F):
	'''
	MEANCURVATURE  computes the mean curvature of a triangle mesh

	Inputs:
    V: |V|-by-3 numpy ndarray of vertex positions
    F: |F|-by-3 numpy ndarray of face indices

    Output:
    H: |V| numpy array of mean curvature at each vertex
	'''
	L = cotmatrix(V,F)
	VA = vertexAreas(V, F)
	inv_M = scipy.sparse.csr_matrix(np.diag(1/(VA+np.finfo(float).eps)))
	L = inv_M * L
	H = np.sqrt(np.sum((-L*V)**2, axis=1)) / 2.0
	return H



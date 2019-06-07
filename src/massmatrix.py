import numpy as np
import scipy
import scipy.sparse 
from vertexAreas import vertexAreas
def massmatrix(V, F):
	"""
	MASSMATRIX computes mass matrix of vertex areas
	Input:
	  V (|V|,3) numpy array of vertex positions
	  F (|F|,3) numpy array of face indices
	Output:
	  M (|V|,|V|) scipy sparse diagonal matrix of vertex area
	"""
	VA = vertexAreas(V,F)
	M = scipy.sparse.csr_matrix(np.diag(VA))
	return M
import numpy as np
import numpy.matlib as matlib
import scipy
import scipy.sparse 
from faceAreas import faceAreas

def vertexAreas(V, F):
	"""
	VERTEXAREAS computes area per vertex (sum of 1/3 adjacent face areas) 

	Input:
	  V (|V|,3) numpy array of vertex positions
	  F (|F|,3) numpy array of face indices
	Output:
	  VA (|V|,) numpy array of vertex area
	"""
	faceArea = faceAreas(V,F)

	rowIdx = F.reshape(F.shape[0]*F.shape[1])
	colIdx = matlib.repmat(np.expand_dims(np.arange(F.shape[0]),axis=1),1,3).reshape(F.shape[0]*F.shape[1])
	data = np.ones([F.shape[0]*F.shape[1]]) / 3.0
	W = scipy.sparse.csr_matrix((data, (rowIdx, colIdx)), shape=(V.shape[0],F.shape[0]))
	return W*faceArea
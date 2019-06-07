import numpy as np
import sys
import scipy
import scipy.sparse 
from normalizeRow import normalizeRow
from faceAreas import faceAreas
import numpy.matlib as matlib

def vertexNormals(V, F):
	"""
	VERTEXNORMALS computes face area weighted vertex normal

	Input:
	  V (|V|,3) numpy array of vertex positions
	  F (|F|,3) numpy array of face indices
	Output:
	  vertNormal (|V|,3) numpy array of normalized vertex normal
	"""
	vec1 = V[F[:,1],:] - V[F[:,0],:]
	vec2 = V[F[:,2],:] - V[F[:,0],:]
	FN = np.cross(vec1, vec2) / 2
	FN_normalized = normalizeRow(FN+sys.float_info.epsilon)
	faceArea = faceAreas(V,F)

	VN = np.zeros(V.shape)
	rowIdx = F.reshape(F.shape[0]*F.shape[1])
	colIdx = matlib.repmat(np.expand_dims(np.arange(F.shape[0]),axis=1),1,3).reshape(F.shape[0]*F.shape[1])
	weightData = matlib.repmat(np.expand_dims(faceArea,axis=1),1,3).reshape(F.shape[0]*F.shape[1])
	W = scipy.sparse.csr_matrix((weightData, (rowIdx, colIdx)), shape=(V.shape[0],F.shape[0]))
	vertNormal = W*FN_normalized
	vertNormal = normalizeRow(vertNormal)
	return vertNormal
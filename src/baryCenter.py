import numpy as np

def baryCenter(V, F):
	'''
	BARYCENTER computes the bary centers of a triangle mesh

	Inputs:
	V: n-by-3 numpy ndarray of vertex positions
	F: m-by-3 numpy ndarray of face indices

	Outputs:
	B: |F|-by-3 numpy ndarray
	'''
	B = np.zeros((F.shape[0],V.shape[1]), dtype = np.float32)
	for ii in range(F.shape[1]):
		B += 1.0/F.shape[1] * V[F[:,ii],:]
	return B
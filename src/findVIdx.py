import numpy as np
import sys

def findVIdx(F, VIdx):
	'''
    FINDVIDX finds desired vertices in the face list

    Inputs:
    F: |F|-by-3 numpy ndarray of face indices
	VIdx: a list of vertex indices

    Output:
    r, c: row/colummn indices in the face list
    '''
	# return the indices of VIdx in F
	mask = np.in1d(F.flatten(),VIdx)
	r = np.floor(np.where(mask)[0] / 3.0).astype(int)
	c = np.where(mask)[0] % 3
	return r,c
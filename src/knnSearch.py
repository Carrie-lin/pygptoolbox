import scipy
import scipy.spatial

def knnSearch(array1, array2, k):
    """
    KNNSEARCH finds the k nearnest neighbors of array1 in array2

    Inputs:
        array1: N-by-D numpy array of query points
        array2: M-by-D numpy array existing points
        k: number of neighbors to return

    Output:
        dist: distance between the point in array1 with kNN
        NNIdx: nearest neighbor indices of array1
    """
    kdtree = scipy.spatial.cKDTree(array2)
    dist, NNIdx = kdtree.query(array1, k)
    return dist, NNIdx
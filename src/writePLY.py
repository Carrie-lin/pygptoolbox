import numpy as np
from colorMap import colorMap

def writePLY(fileName,V,F,VC = None, colormap = 'default'):
    f = open(fileName, 'w')

    # headers
    string = 'ply\n'
    string = string + 'format ascii 1.0\n'
    string = string + 'element vertex ' + str(V.shape[0]) + '\n'
    string = string + 'property double x\n'
    string = string + 'property double y\n'
    string = string + 'property double z\n'

    # color map
    if (VC is not None and VC.shape[0] == V.shape[0]):
        color = colorMap(VC, colormap = colormap)
        color = (color*255).astype(np.uint8)
        string = string + 'property uchar red\n'
        string = string + 'property uchar green\n'
        string = string + 'property uchar blue\n'
        string = string + 'property uchar alpha\n'
    
    # end of header
    string = string + 'element face ' + str(F.shape[0]) + '\n'
    string = string + 'property list int int vertex_indices\n'
    string = string + 'end_header\n'
    f.write(string)

    # write vertices    
    for ii in range(V.shape[0]):
        string = '%f %f %f ' % (V[ii,0], V[ii,1], V[ii,2])
        if (VC is not None and VC.shape[0] == V.shape[0]):
            string = string + '%03d %03d %03d %03d\n' % (color[ii,0], color[ii,1], color[ii,2], 255)
        else:
            string = string + '\n'
        f.write(string)
    for ii in range(F.shape[0]):
        string = '%d %d %d %d\n' % (3, F[ii,0], F[ii,1], F[ii,2])
        f.write(string)
    f.close()

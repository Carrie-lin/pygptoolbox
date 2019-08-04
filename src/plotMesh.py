import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3
import numpy as np

from colorMap import colorMap
from faceNormals import faceNormals

def plotMesh(V,F, \
    c=np.array([0]),\
    colormap='default',\
    showEdges=False):
    
    # compute colors for rendering
    FN = faceNormals(V,F)
    z = (FN[:,2] + 2) / 3
    if (c.shape[0] != V.shape[0]):
        face_color = np.array([144.0/ 255.0, 210.0/ 255.0, 236.0/ 255.0])
        face_color = z[:,None]*face_color
    else:
        # colormap: "blue", "red", "green", "default"
        cf = (c[F[:,0]] + c[F[:,1]] + c[F[:,2]]) / 3.0
        face_color = colorMap(cf, colormap = colormap, valRange = None)
        face_color = z[:,None]*face_color

    # open a figure
    fig = plt.figure(figsize=(7, 7))
    ax = fig.gca(projection='3d')

    # get vertices 
    vtx = V[F,:]
    
    # plot
    if showEdges == True:
        mesh = a3.art3d.Poly3DCollection(vtx, linewidths=.5,  edgecolors=[0,0,0])
    else:
        mesh = a3.art3d.Poly3DCollection(vtx)
    
    # add face color
    mesh.set_facecolor(face_color)
    
    # add mesh to figures
    ax.add_collection3d(mesh)

    # set figure axis 
    axisRange = np.array([np.max(V[:,0])-np.min(V[:,0]), np.max(V[:,1])-np.min(V[:,1]), np.max(V[:,2])-np.min(V[:,2])])
    r = np.max(axisRange) / 2.0
    mean = np.mean(V, 0)
    ax.set_xlim(mean[0]-r, mean[0]+r)
    ax.set_ylim(mean[1]-r, mean[1]+r)
    ax.set_zlim(mean[2]-r, mean[2]+r)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show() 

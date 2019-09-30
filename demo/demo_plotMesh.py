import sys
sys.path.append('../src')

from plotMesh import plotMesh
from readOBJ import readOBJ

V,F = readOBJ('../meshes/bunny.obj')
plotMesh(V,F,showEdges = True)
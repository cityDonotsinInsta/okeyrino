from pygame as pg
from matrix_functions import *

class Object3D:
    def __init__(self, render):
        self.render = render
        self.vertexes = np.array([(0,0,0,1),(0,1,0,1),(1,1,0,1),(1,0,0,1),
                                  (0,0,1,1),(0,1,1,1),(1,1,1,1),(1,0,1,1)])
        self.faces = np.array([(0,1,2,3),(2,3,6,7),(4,5,6,7),(0,1,4,5),(1,2,5,6),(0,3,4,7)])

    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    def  
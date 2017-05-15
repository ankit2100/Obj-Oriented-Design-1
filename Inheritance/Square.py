__author__ = 'ankit.b.patel'
from Shape import Shape
class Square(Shape):

    def __init__(self):
        Shape.__init__(self,4,5,0)
    def getArea(self):
        return self.length * self.width
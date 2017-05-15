__author__ = 'ankit.b.patel'
from Shape import Shape
class Circle(Shape):

    def __init__(self):
        Shape.__init__(self,0,0,4)
        pass
    def getArea(self):
        return 3.14 * self.radious * self.radious
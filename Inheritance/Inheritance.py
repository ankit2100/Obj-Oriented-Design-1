__author__ = 'ankit.b.patel'
class Shape():
    def __init__(self,length=0,width=0,radious=0):
        self.length = length
        self.width = width
        self.radious = radious
    def printDimentions(self):
        print self.length
        print self.width

class Circle(Shape):

    def __init__(self):
        Shape.__init__(self,0,0,4)
        pass
    def getArea(self):
        return 3.14 * self.radious * self.radious

class Square(Shape):

    def __init__(self):
        Shape.__init__(self,4,5,0)
    def getArea(self):
        return self.length * self.width

cir = Circle()
print cir.getArea()
sq = Square()
print sq.getArea()

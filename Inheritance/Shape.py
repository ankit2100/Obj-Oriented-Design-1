__author__ = 'ankit.b.patel'
class Shape():
    def __init__(self,length=0,width=0,radious=0):
        self.length = length
        self.width = width
        self.radious = radious
    def printDimentions(self):
        print self.length
        print self.width

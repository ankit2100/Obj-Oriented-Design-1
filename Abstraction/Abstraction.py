__author__ = 'ankit.b.patel'
class AbstractClass():
   def Area(self):
      raise NotImplementedError("Subclass must implement abstract method")

class Graph(AbstractClass):
    def __init__(self):
        self.len = 10
        self.wid = 20
    def Area(self):
        return self.len * self.wid

g = Graph()
print g.Area()
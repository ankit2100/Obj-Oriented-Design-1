__author__ = 'ankit.b.patel'
class Encapsulation(object):
    def __init__(self, a, b, c):

        self.public = a
        self._protected = b
        self.__private = c
        Encapsulation.staticvar = 0 #static var
    def AccessPrivateMembers(self):
        return self.__private

print Encapsulation.staticvar

e = Encapsulation(10,20,30)
print e.public
print e._protected #I feel like having no diff between public and protected membors.
print e.AccessPrivateMembers()

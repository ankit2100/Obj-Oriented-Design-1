__author__ = 'ankit.b.patel'
class Bear(object):
    def sound(self,noise="Groarrr"):
        print noise

bearObj = Bear()

bearObj.sound() #sounds basic noise "Groarrr"
bearObj.sound("bow bow") #souds "bow bow"
class Facette:
    def __init__(self, force, coord):
        self.__force = force
        self.__coord = coord

    def GetForce(self):
        return self.__force

    def GetCoord(self):
        return self.__coord

    def SetForce(self,force):
        self.__force = force

    def SetCoord(self,coord):
        self.__coord = coord

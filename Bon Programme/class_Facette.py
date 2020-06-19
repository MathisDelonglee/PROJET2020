class Facette:
    def __init__(self, force, coordonnees, surface):
        self.__force = force
        self.__coordonnees = coordonnees
        self.__surface = surface

    def GetForce(self):
        return self.__force

    def GetCoordonnees(self):
        return self.__coordonnees

    def GetSurface(self):
        return self.__surface

    def SetCoordonnes(self, coordonnes):
        self.__coordonnees = coordonnes

    def SetForce(self, force):
        self.__force = force

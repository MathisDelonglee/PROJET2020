import Recuperation_Donnees as rd
from class_Facette import *
import math as mt

def Vectoriel(a, b):
    c = [a[1] * b[2] - a[2] * b[1],
         a[2] * b[0] - a[0] * b[2],
         a[0] * b[1] - a[1] * b[0]]

    return c


def Surface(liste):
    Ax = float(liste[1][0])
    Ay = float(liste[1][1])
    Az = float(liste[1][2])
    Bx = float(liste[2][0])
    By = float(liste[2][1])
    Bz = float(liste[2][2])
    Cx = float(liste[3][0])
    Cy = float(liste[3][1])
    Cz = float(liste[3][2])

    AB = Bx - Ax, By - Ay, Bz - Az
    AC = Cx - Ax, Cy - Ay, Cz - Az

    vect = Vectoriel(AB, AC)
    norme = mt.sqrt(vect[0]**2+vect[1]**2+vect[2]**2)

    return (norme/2)*float(liste[0][0]), (norme/2)*float(liste[0][1]), (norme/2)*float(liste[0][2])


def Poussee_Archimede(coor_z, surface):

    return coor_z * surface[0], coor_z * surface[1], coor_z * surface[2]


def CentreFacette(D):
    z1, z2, z3 = float(D[1][2]), float(D[2][2]), float(D[3][2])
    y1, y2, y3 = float(D[1][1]), float(D[2][1]), float(D[3][1])
    x1, x2, x3 = float(D[1][0]), float(D[2][0]), float(D[3][0])

    moyz = (z1 + z2 + z3) / 3
    moyy = (y1 + y2 + y3) / 3
    moyx = (x1 + x2 + x3) / 3

    return moyx, moyy, moyz

def translation(liste_facette):
    u = [0, 0, -1]

    for elt in liste_facette:
        print(elt.GetCoord())
        for i in elt.GetCoord():
            for j in range(3):
                i[j] = float(i[j]) + u[j]

        print(elt.GetCoord())
    return liste_facette


def Force_Archimede_Total(liste_facette):
    g = 9.81

    ro = 1025
    F = [0, 0, 0]
    for elt in liste_facette:
        F[0] += elt.GetForce()[0]
        F[1] += elt.GetForce()[1]
        F[2] += elt.GetForce()[2]

    return F[0] * g * ro, F[1] * g * ro, F[2] * g * ro


Donnes_facettes = rd.RecupDonnee()
liste_facette = []
longueur = len(Donnes_facettes)
for i in range(longueur):
    D = Donnes_facettes[i]
    S = Surface(D)
    centre = CentreFacette(D)

    force = Poussee_Archimede(centre[2], S)  # centre[2] correspond au z
    liste_facette.append(Facette(force, D[1:]))  # création de l'objet Facette

print(Force_Archimede_Total(liste_facette))
liste_facette = translation(liste_facette)
print(Force_Archimede_Total(liste_facette))

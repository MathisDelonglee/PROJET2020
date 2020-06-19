import Recuperation_Donnees as rd
from class_Facette import *
import matplotlib.pyplot as plt

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

    AB = [Bx - Ax, By - Ay, Bz - Az]
    AC = [Cx - Ax, Cy - Ay, Cz - Az]

    vect = Vectoriel(AB, AC)
    #norme = mt.sqrt(abs(vect[0]) + abs(vect[1]) + abs(vect[2]))
    #return [(norme / 2) * liste[0][0], (norme / 2) * liste[0][1], (norme / 2) * liste[0][2]]
    return vect[0]/2, vect[1]/2, vect[2]/2


def Poussee_Archimede(coor_z, surface):
    if coor_z <= 0:
        return [coor_z * surface[0], coor_z * surface[1], coor_z * surface[2]]
    else:
        return [0, 0, 0]


def CentreFacette(D):
    z1, z2, z3 = float(D[0][2]), float(D[1][2]), float(D[2][2])
    y1, y2, y3 = float(D[0][1]), float(D[1][1]), float(D[2][1])
    x1, x2, x3 = float(D[0][0]), float(D[1][0]), float(D[2][0])

    moyz = (z1 + z2 + z3) / 3
    moyy = (y1 + y2 + y3) / 3
    moyx = (x1 + x2 + x3) / 3

    return moyx, moyy, moyz


def Force_Archimede_Total(liste_facette, ro):
    g = 9.81
    F = [0, 0, 0]
    for elt in liste_facette:
        F[0] += elt.GetForce()[0]
        F[1] += elt.GetForce()[1]
        F[2] += elt.GetForce()[2]

    return [F[0] * g * ro, F[1] * g * ro, F[2] * g * ro]


def Translation(liste_facette, u):
    for elt in liste_facette:
        for i in elt.GetCoordonnees():
            for j in range(3):
                i[j] = float(i[j]) + u[j]
        centre = CentreFacette(elt.GetCoordonnees())
        elt.SetForce(Poussee_Archimede(centre[2], elt.GetSurface()))
    return liste_facette


def CalculTirantDeau(liste_facette):
    z = 100
    for elt in liste_facette:
        coord = elt.GetCoordonnees()
        for elt2 in coord:
            if elt2[2] < z:
                z = elt2[2]
    if z >= 0:
        print("Le bateau n'est pas dans l'eau, il n'a pas de tirant d'eau")
        return z
    else:
        return abs(z)


def dichotomie(liste_facette, POIDS_BATEAU, epsilon, ro):
    g = 9.81
    Zga = -10
    Zgb = 10
    compt = 0
    tirantDeau = []
    resforce = []
    while abs(Zgb-Zga) > epsilon:
        Zgmoyen = (Zga+Zgb)/2
        F = abs(Force_Archimede_Total(Translation(liste_facette, [0, 0, Zgmoyen]), ro)[2]) - abs(POIDS_BATEAU*g)
        liste_facette = Translation(liste_facette,[0, 0, -Zgmoyen])  # On enlève la translation aux facettes du bateaux pour les remettre en 0 en z
        Fa = abs(Force_Archimede_Total(Translation(liste_facette, [0, 0, Zga]), ro)[2]) - abs(POIDS_BATEAU*g)
        liste_facette = Translation(liste_facette,[0, 0, -Zga])  # On enlève la translation aux facettes du bateaux pour les remettre en 0 en z
        if F*Fa < 0:
            Zgb = Zgmoyen
        else:
            Zga = Zgmoyen
        resforce.append(F)
        compt += 1
        liste_facette = Translation(liste_facette, [0, 0, Zga])
        tirantDeau.append(CalculTirantDeau(liste_facette))
        liste_facette = Translation(liste_facette, [0, 0, -Zga])
    return tirantDeau, resforce

#*****Main*******

def Main(POID_BATEAU, fichier, epsilon, ro):
    #POID_BATEAU = 700   # en kg
    Donnes_facettes = rd.RecupDonnee(fichier)
    liste_facette = []
    CentreBateauZ = 0
    longueur = len(Donnes_facettes)
    for i in range(longueur):
        D = Donnes_facettes[i]  # [normale,pointA, pointB, PointC]
        S = Surface(D)  # retourne AB ^ AC /2
        centre = CentreFacette(D[1:])[2]  #retourne les coordonnes du centre de la facette
        CentreBateauZ += centre
        force = Poussee_Archimede(centre, S)  # centre correspond à la moyenne du z de la facette
        liste_facette.append(Facette(force, D[1:], S))  # création des objets Facette

    CentreBateauZ = CentreBateauZ/longueur
    liste_facette = Translation(liste_facette, [0, 0, -CentreBateauZ])  #On place le point central du bateau suivant l'axe z à 0

    Force_Archimede = Force_Archimede_Total(liste_facette, ro)

    print("Force D'archimede s'éxerçant sur le bateau en son centre z=0 :\n\tX : ", Force_Archimede[0], '\n\tY : ', Force_Archimede[1], '\n\tZ : ', Force_Archimede[0])
    print("Son tirant d'eau est d'actuellement : ", CalculTirantDeau(liste_facette), ' m')

    a = dichotomie(liste_facette, POID_BATEAU, epsilon, ro)
    print("\n*************************")
    print("Après calcul, son tirant d'eau pour que le bateau flotte est de : ", a[0][-1], 'm')
    #print(dichotomie(liste_facette, POID_BATEAU))
    return a[1], a[0][-1]



def Recup(fichier):
    contenu = fichier.readlines()
    #print(contenu)
    longueur = len(contenu)
    #print(longueur)
    ListeEntiere = []
    for i in range(0,longueur):
        VectPt = []
        if contenu[i][:14] == '  facet normal':
            VectPt.append(contenu[i][15:-1])
            VectPt.append(contenu[i+2][13:-1])
            VectPt.append(contenu[i+3][13:-1])
            VectPt.append(contenu[i+4][13:-1])
            #print(VectPt)
            ListeEntiere.append(VectPt)


    for i in range(len(ListeEntiere)):
        for y in range(len(ListeEntiere[i])):
            a = ListeEntiere[i][y].split(' ')
            ListeEntiere[i][y] = a
    fichier.close()

    return ListeEntiere

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def CalcFo(ListeEntiere):
    Force = 0
    VectForce = [0,0,0]
    L =ListeEntiere[0]

    #Zg=(float(L[1][2])+float(L[2][2])+float(L[3][2]))/3
    Zg=1
    VectAB = [float(L[2][0])-float(L[1][0]),float(L[2][1])-float(L[1][1]),float(L[2][2])-float(L[1][2])]
    VectAC = [float(L[3][0])-float(L[1][0]),float(L[3][1])-float(L[1][1]),float(L[3][2])-float(L[1][2])]
    #print(VectAC)
    #print(VectAB)
    pv = cross(VectAB,VectAC)
    #print(pv)
    rau = 1000
    dS=((pv[0]**2+pv[1]**2+pv[2]**2)**(1/2))/2
    print('Surface facette:',dS)
    p = rau*9.81*Zg
    print('pression:', p)
    Force += abs(p*dS)
    VectForce[0]+=Force*float(L[0][0])
    VectForce[1]+=Force*float(L[0][1])
    VectForce[2]+=Force*float(L[0][2])
    return Force, VectForce


fichierSTL = open("FichierTestTriRect45.txt","r")

ListeEntiere = Recup(fichierSTL)
print('Facette :',ListeEntiere)
a ,b = CalcFo(ListeEntiere)
print("Norme de la force d'archimède:",a)
print("Vecteur de la force d'archimède :",b)

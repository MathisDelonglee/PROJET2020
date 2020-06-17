
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

def translation(Liste,U):

    for i in range(len(Liste)):
        for j in range(1,4):
            Liste[i][j][0] = str(float(Liste[i][j][0]) + U[0])
            Liste[i][j][1] = str(float(Liste[i][j][1]) + U[1])
            Liste[i][j][2] = str(float(Liste[i][j][2]) + U[2])
    return Liste

def CalcFo(ListeEntiere):
    ForceA = [0,0,0]
    for i in range(len(ListeEntiere)):


        Zg=(float(ListeEntiere[i][1][2])+float(ListeEntiere[i][2][2])+float(ListeEntiere[i][3][2]))/3
        VectAB = [float(ListeEntiere[i][2][0])-float(ListeEntiere[i][1][0]),float(ListeEntiere[i][2][1])-float(ListeEntiere[i][1][1]),float(ListeEntiere[i][2][2])-float(ListeEntiere[i][1][2])]
        VectAC = [float(ListeEntiere[i][3][0])-float(ListeEntiere[i][1][0]),float(ListeEntiere[i][3][1])-float(ListeEntiere[i][1][1]),float(ListeEntiere[i][3][2])-float(ListeEntiere[i][1][2])]
        #print(VectAC)
        #print(VectAB)
        pv = cross(VectAB,VectAC)
        #print(pv)
        dS=((pv[0]**2+pv[1]**2+pv[2]**2)**(1/2))/2
        #print(dS)
        rau = 1025
        if (float(ListeEntiere[i][1][2])and float(ListeEntiere[i][2][2])and float(ListeEntiere[i][3][2]))<0:
            rau = 1025
            ForceA[0]+=rau*9.81*Zg*dS*float(ListeEntiere[i][0][0])
            ForceA[1]+=rau*9.81*Zg*dS*float(ListeEntiere[i][0][1])
            ForceA[2]+=rau*9.81*Zg*dS*float(ListeEntiere[i][0][2])
        elif (float(ListeEntiere[i][1][2])and float(ListeEntiere[i][2][2])and float(ListeEntiere[i][3][2]))>=0:
            pass
        else:
            if (float(ListeEntiere[i][1][2])+ float(ListeEntiere[i][2][2])+ float(ListeEntiere[i][3][2]))/3>0:
                pass
            else:
                rau = 1025
                ForceA[0]+=rau*9.81*Zg*dS*float(ListeEntiere[i][0][0])
                ForceA[1]+=rau*9.81*Zg*dS*float(ListeEntiere[i][0][1])
                ForceA[2]+=rau*9.81*Zg*dS*float(ListeEntiere[i][0][2])



    print(ForceA)
    return ForceA


fichierSTL = open("V_HULL_note.txt","r")

ListeEntiere = Recup(fichierSTL)
z=-0.5

U=[0, 0, z]

CalcFo(ListeEntiere)
L = translation(ListeEntiere,U)
CalcFo(L)



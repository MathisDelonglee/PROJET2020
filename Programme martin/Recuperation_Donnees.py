def RecupDonnee():
    fichier = open("V_HULL_note.txt", "r")

    contenu = fichier.readlines()
    longueur = len(contenu)
    ListeEntiere = []
    for i in range(0, longueur):
        VectPt = []
        if contenu[i][:14] == '  facet normal':
            VectPt.append(contenu[i][15:-1])
            VectPt.append(contenu[i + 2][13:-1])
            VectPt.append(contenu[i + 3][13:-1])
            VectPt.append(contenu[i + 4][13:-1])
            ListeEntiere.append(VectPt)

    for i in range(len(ListeEntiere)):  # Tri de la liste pour mieux se repérer
        for y in range(len(ListeEntiere[i])):
            a = ListeEntiere[i][y].split(' ')
            ListeEntiere[i][y] = a

    return ListeEntiere
RecupDonnee()

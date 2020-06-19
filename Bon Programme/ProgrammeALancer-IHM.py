from PySide2.QtWidgets import *
from stl import mesh
from PySide2.QtGui import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Force_Archimede import *

class Test(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        #ajout titre et icone fenêtre
        self.setWindowTitle("Boat sinking interface")
        self.icon = QIcon("boat.png")
        self.setWindowIcon(self.icon)

        #creation layout
        self.layout = QGridLayout()

        #creation des figures
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = mplot3d.Axes3D(self.fig)
        self.fig2 = plt.figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.axes2 = plt.axes()

        #creations des boutons, zones de texte, entrée utilisateur
        self.result = QLabel("")
        self.textmasse = QLabel("Entrer une valeur pour la masse du navire (en kg) :")
        self.texteeau = QLabel("Choisir entre ces deux options :")
        self.masse = QLineEdit()
        self.text = QLabel('Entrer la précision souhaitée :')
        self.espace = QLabel('')
        self.button = QPushButton("Valider")
        self.roeaudouce = QPushButton('Eau douce')
        self.roeausalee = QPushButton('Eau salée')
        self.espace2 = QLabel('')
        self.preci = QLineEdit()
        self.boatchoice = QLabel("Cliquer sur la forme de navire que vous voulez étudier :")
        self.button1 = QPushButton('Rectangulaire')
        self.button2 = QPushButton('Navire Mini650')
        self.button3 = QPushButton('Barge en Aluminium')
        self.button4 = QPushButton('Sous marin')

        #ajout des widgets dans le layout
        self.layout.addWidget(self.textmasse,0,0)
        self.layout.addWidget(self.text,1,0)
        self.layout.addWidget(self.texteeau,2,0)
        self.layout.addWidget(self.masse,0,1)
        self.layout.addWidget(self.preci,1,1)
        self.layout.addWidget(self.button,0,2,2,2)
        self.layout.addWidget(self.roeaudouce, 2, 1, 1, 1 )
        self.layout.addWidget(self.roeausalee, 2, 2, 1, 2 )
        self.layout.addWidget(self.boatchoice,4,0,1,2)
        self.layout.addWidget(self.espace,3,1)
        self.layout.addWidget(self.espace2,6,0)
        self.layout.addWidget(self.result,7,0)
        self.layout.addWidget(self.button1,5,0)
        self.layout.addWidget(self.button2,5,1)
        self.layout.addWidget(self.button3,5,2)
        self.layout.addWidget(self.button4,5,3)

        self.setLayout(self.layout)

        #fonctionnalités lorsque l'on clique sur un bouton
        self.button.clicked.connect(self.valider)
        self.roeaudouce.clicked.connect(self.validrodouce)
        self.roeausalee.clicked.connect(self.validrosalee)
        self.button1.clicked.connect(self.fonct1)
        self.button2.clicked.connect(self.fonct2)
        self.button3.clicked.connect(self.fonct3)
        self.button4.clicked.connect(self.fonct4)


    def validrodouce(self): #rhô eau douce
        self.ro = 1000
        return

    def validrosalee(self): #rhô eau salée
        self.ro = 1025
        return

    def valider(self):
        self.poids = float(self.masse.text())*9.81/10
        self.precision =float(self.preci.text())
        return

    def fonct1(self):
        #suppresion des données précédentes s'il y en a
        self.result.clear()
        self.axes.clear()
        self.axes2.clear()

        self.axes.set_title('Maquette du bateau choisi') #titre maquette
        self.setMinimumSize(960, 520) #taille fenêtre
        your_mesh = mesh.Mesh.from_file('Rectangular_HULL_Normals_Outward.STL') #lien maquette format stl
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2) #ajout canvas au layout
        a,b = Main(self.poids, 'Rectangular_HULL_note.txt',self.precision,self.ro) #lien fichier format txt
        self.axes2.set_title("Résultante des forces / Nombre d'itérations") #titre graph
        self.axes2.plot(a)
        self.canvas2.draw() #dessin canvas
        self.layout.addWidget(self.canvas2,8,2,2,2) #ajout canvas au layout
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m") #message tirant d'eau
        self.layout.addWidget(self.result,7,0) # ajout message au layout
        return

#même code pour les 4 fonctions



    def fonct2(self): #affichage Maquette et graphique

        self.result.clear()
        self.axes.clear()
        self.axes2.clear()
        self.axes.set_title('Maquette du bateau choisi')
        self.setMinimumSize(960,520)
        your_mesh = mesh.Mesh.from_file('Mini650_HULL_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2)
        a,b = Main(self.poids, 'Mini650_HULL_note.txt',self.precision, self.ro)
        self.axes2.set_title("Résultante des forces / Nombre d'itérations")
        self.axes2.plot(a)
        self.canvas2.draw()
        self.layout.addWidget(self.canvas2,8,2,2,2)
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m")
        self.layout.addWidget(self.result,7,0)
        return

    def fonct3(self): #affichage Maquette et graphique

        self.result.clear()
        self.axes.clear()
        self.axes2.clear()
        self.axes.set_title('Maquette du bateau choisi')
        self.setMinimumSize(960, 520)
        your_mesh = mesh.Mesh.from_file('BargeAlu_L_2980_W_633_H_400_NormalOutward2.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2)
        a, b = Main(self.poids, 'BargeAlu_L_2980_W_633_H_400_NormalOutward2_note.txt', self.precision, self.ro)
        self.axes2.set_title("Résultante des forces / Nombre d'itérations")
        self.axes2.plot(a)
        self.canvas2.draw()
        self.layout.addWidget(self.canvas2,8,2,2,2)
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m")
        self.layout.addWidget(self.result,7,0)
        return

    def fonct4(self):

        self.result.clear()
        self.axes.clear()
        self.axes2.clear()
        self.axes.set_title('Maquette du bateau choisi')
        self.setMinimumSize(960, 520)
        your_mesh = mesh.Mesh.from_file('ssmarin_L=4_W=2_H=2_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2)
        a,b = Main(self.poids, 'ssmarin_L=4_W=2_H=2_Normals_Outward_note.txt',self.precision, self.ro)
        self.axes2.set_title("Résultante des forces / Nombre d'itérations")
        self.axes2.plot(a)
        self.canvas2.draw()
        self.layout.addWidget(self.canvas2,8,2,2,2)
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m")
        self.layout.addWidget(self.result,7,0)
        return

if __name__== '_main_': #si l'IHM ne s'affiche pas, enlever le [if __name__ == '_main_']
    app = QApplication([])
    ihm = Test()
    ihm.show()
    app.exec_()


from PySide2.QtWidgets import *
from PySide2.QtGui import *
import matplotlib.pyplot as plt
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Force_Archimede import *
#from testgraphique import *

class Test(QWidget,QApplication):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.layout1 = QHBoxLayout()

        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = mplot3d.Axes3D(self.fig)
        self.fig2 = plt.figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.axes2 = plt.axes()

        self.result = QLabel("")
        self.textmasse = QLabel("Entrez une valeur pour la masse du navire (en kg) :")
        self.masse = QLineEdit()
        self.text = QLabel('Entrez la précision :')
        self.espace = QLabel('')
        self.espace2 = QLabel('')
        self.preci = QLineEdit()
        self.button = QPushButton("Valider")
        self.textchoice = QLabel("Cliquez sur la forme de navire que vous voulez étudier")
        self.roeaudouce = QPushButton('Eau douce')
        self.roeausalee = QPushButton('Eau salée')
        self.button1 = QPushButton('Triangulaire')
        self.button2 = QPushButton('Rectangulaire')
        self.button3 = QPushButton('Cylindrique')
        self.button4 = QPushButton('Navire Mini650')
        #self.textpresentation = QLabel("Voici la maquette du navire choisi")
        self.layout.addWidget(self.result,7,0)
        self.layout.addWidget(self.textmasse,0,0)
        self.layout.addWidget(self.masse,0,1)
        self.layout.addWidget(self.button,0,2,2,2)
        self.layout.addWidget(self.textchoice,4,1, 1, 2)
        #self.layout.addWidget(self.textpresentation,7,1, 1, 2)
        self.layout.addWidget(self.text,1,0)
        self.layout.addWidget(self.preci,1,1)
        self.layout.addWidget(self.roeaudouce, 2, 1, 1, 1 )
        self.layout.addWidget(self.roeausalee, 2, 2, 1, 2 )
        self.layout.addWidget(self.espace,3,1)

        self.layout.addWidget(self.button1,5,0)
        self.layout.addWidget(self.button2,5,1)
        self.layout.addWidget(self.button3,5,2)
        self.layout.addWidget(self.button4,5,3)
        self.layout.addWidget(self.espace2,6,0)


        self.setLayout(self.layout)

        self.roeaudouce.clicked.connect(self.validrodouce)
        self.roeausalee.clicked.connect(self.validrosalee)
        self.button.clicked.connect(self.valider)
        self.button4.clicked.connect(self.fonct4)
        self.button3.clicked.connect(self.fonct3)
        self.button2.clicked.connect(self.fonct2)
        self.button1.clicked.connect(self.fonct1)

    def validrodouce(self):
        self.ro = 1000
        return

    def validrosalee(self):
        self.ro = 1025
        return

    def valider(self):
        self.poids = float(self.masse.text())*9.81/10
        self.precision =float(self.preci.text())
        return

    def fonct4(self):
        #self.layout.addWidget(self.textpresentation,7,0, 1, 2)
        self.result.clear()
        self.axes.clear()
        self.axes2.clear()
        self.axes.set_title('Maquette du bateau choisi')
        self.setMinimumSize(800,500)
        your_mesh = mesh.Mesh.from_file('Mini650_HULL_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2)
        a,b = Main(self.poids, 'Mini650_HULL_note.txt',self.precision, self.ro)
        #self.canvas2.set_window_title("Résultante des forces en fonction du temps")
        #plt.title("Résultante des forces en fonction du temps")
        self.axes2.set_title("Résultante des forces en fonction du nombre d'itération")
        self.axes2.set_ylabel('Résultante des forces')
        self.axes2.set_xlabel("Nombre d'itération")
        self.axes2.plot(a)
        self.canvas2.draw()
        self.layout.addWidget(self.canvas2,8,2,2,2)
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m")
        self.layout.addWidget(self.result,7,0)

        return

    def fonct3(self):
        #self.layout.addWidget(self.textpresentation,7,0, 1, 2)
        self.result.clear()
        self.axes.clear()
        self.axes2.clear()
        self.axes.set_title('Maquette du bateau choisi')
        self.setMinimumSize(800,500)
        your_mesh = mesh.Mesh.from_file('Cylindrical_HULL_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2)
        a, b = Main(self.poids, 'Cylindrical_HULL_note.txt', self.precision, self.ro)
        self.axes2.set_title("Résultante des forces en fonction du nombre d'itération")
        self.axes2.set_ylabel('Résultante des forces')
        self.axes2.set_xlabel("Nombre d'itération")
        self.axes2.plot(a)
        self.canvas2.draw()
        self.layout.addWidget(self.canvas2,8,2,2,2)
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m")
        self.layout.addWidget(self.result,7,0)
        return

    def fonct2(self):
        #self.layout.addWidget(self.textpresentation,7,0, 1, 2)
        self.result.clear()
        self.axes.clear()
        self.axes2.clear()
        self.axes.set_title('Maquette du bateau choisi')
        self.setMinimumSize(800,500)
        your_mesh = mesh.Mesh.from_file('Rectangular_HULL_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2)
        a,b = Main(self.poids, 'Rectangular_HULL_note.txt',self.precision,self.ro)
        self.axes2.set_title("Résultante des forces en fonction du nombre d'itération")
        self.axes2.set_ylabel('Résultante des forces')
        self.axes2.set_xlabel("Nombre d'itération")
        self.axes2.plot(a)
        self.canvas2.draw()
        self.layout.addWidget(self.canvas2,8,2,2,2)
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m")
        self.layout.addWidget(self.result,7,0)


        return

    def fonct1(self):
        #self.layout.addWidget(self.textpresentation,7,0, 1, 2)
        self.result.clear()
        self.axes.clear()
        self.axes2.clear()
        self.axes.set_title('Maquette du bateau choisi')
        self.setMinimumSize(800, 500)
        your_mesh = mesh.Mesh.from_file('V_HULL_Normals_Outward.STL')
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
        scale = your_mesh.points.flatten('F')
        self.axes.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,8,0,2,2)
        a,b = Main(self.poids, 'V_HULL_note.txt',self.precision, self.ro)
        self.axes2.set_title("Résultante des forces en fonction du nombre d'itération")
        self.axes2.set_ylabel('Résultante des forces')
        self.axes2.set_xlabel("Nombre d'itération")
        self.axes2.plot(a)
        self.canvas2.draw()
        self.layout.addWidget(self.canvas2,8,2,2,2)
        self.result = QLabel("Le tirant d'eau du bateau à l'équilibre est de "+str(round(b,4))+" m")
        self.layout.addWidget(self.result,7,0)

        return

app = QApplication([])
ihm = Test()
ihm.show()
app.exec_()

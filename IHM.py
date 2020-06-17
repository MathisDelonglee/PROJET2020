
from PySide2.QtWidgets import *


class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Boat sinkink interface")
        self.setMinimumSize(500,200)
        self.layout = QHBoxLayout()

        self.Label = QLabel("poid de votre coque de bateau:")
        self.layout.addWidget(self.Label)
        self.text = QLineEdit('')
        self.layout.addWidget(self.text)
        self.button1 = QPushButton('Calculer')
        self.layout.addWidget(self.button1)




        self.button1.clicked.connect(self.buttonCliqued)

        self.setLayout(self.layout)

    def buttonCliqued(self):
        self.setMinimumSize(1000,500)
        self.Label = QLabel("poid de votre coque de bateau:")
        self.layout.addWidget(self.Label)



if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM()
   ihm.show()
   app.exec_()

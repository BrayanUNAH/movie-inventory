# -*- coding: 'utf-8' -*_
import sys
from Núcleo.MainWindow import *


class GraphicInterface(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = GraphicInterface()
    window.show()
    app.exec_()



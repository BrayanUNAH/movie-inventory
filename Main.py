# -*- coding: 'utf-8' -*_
from LinkedList import LinkedList
from Movie import Movie
import sys
from MainWindow import *
from AddWindow import *
from EditWindow import *

class GraphicInterface(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    movieList = LinkedList()
    app = QtWidgets.QApplication([])
    window = GraphicInterface()
    window.show()
    app.exec_()



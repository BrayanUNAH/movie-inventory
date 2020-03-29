import sys
from MainWindow import *
from AddWindow import *
from EditWindow import *


class GraphicInterface(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = GraphicInterface()
    window.show()
    app.exec_()

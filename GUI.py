import sys
from MainWindow import *
from AddWindow import *
from EditWindow import *

class GUI(QtWidgets.QMainWindow, MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonAddMovie.clicked.connect(self.addWindow)
        self.buttonViewAndEditListing.clicked.connect(self.editWindow)
        
    def addWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        print(self.ui.textDescription.toPlainText())
        

    def editWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = EditWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = GUI()
    window.show()
    app.exec_()

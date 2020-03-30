# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from AddWindow import AddWindow
from EditWindow import EditWindow
from LinkedList import LinkedList

class MainWindow(object):

    def __init__(self):
        self.movieList = LinkedList()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(388, 544)
        self.buttonAddMovie = QtWidgets.QPushButton(Dialog)
        self.buttonAddMovie.setGeometry(QtCore.QRect(80, 300, 221, 61))
        self.buttonAddMovie.setObjectName("buttonAddMovie")
        self.buttonViewAndEditListing = QtWidgets.QPushButton(Dialog)
        self.buttonViewAndEditListing.setGeometry(QtCore.QRect(80, 380, 221, 61))
        self.buttonViewAndEditListing.setObjectName("buttonViewAndEditListing")
        self.buttonViewTree = QtWidgets.QPushButton(Dialog)
        self.buttonViewTree.setGeometry(QtCore.QRect(80, 460, 221, 61))
        self.buttonViewTree.setObjectName("buttonViewTree")
        self.buttonAbout = QtWidgets.QPushButton(Dialog)
        self.buttonAbout.setGeometry(QtCore.QRect(280, 10, 101, 31))
        self.buttonAbout.setObjectName("buttonAbout")
        self.labelMoviesInTotal = QtWidgets.QLabel(Dialog)
        self.labelMoviesInTotal.setGeometry(QtCore.QRect(50, 210, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelMoviesInTotal.setFont(font)
        self.labelMoviesInTotal.setObjectName("labelMoviesInTotal")
        self.labelNumberOfMovies = QtWidgets.QLabel(Dialog)
        self.labelNumberOfMovies.setGeometry(QtCore.QRect(170, 80, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.labelNumberOfMovies.setFont(font)
        self.labelNumberOfMovies.setObjectName("labelNumberOfMovies")
        self.retranslateUi(Dialog)
        
        self.buttonAddMovie.clicked.connect(self.addWindow)
        self.buttonViewAndEditListing.clicked.connect(self.editWindow)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def addWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddWindow(self.movieList)
        self.ui.setupUi(self.window)
        self.window.show()

    def editWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = EditWindow(self.movieList)
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ventana Principal"))
        self.buttonAddMovie.setText(_translate("Dialog", "Agregar"))
        self.buttonViewAndEditListing.setText(_translate("Dialog", "Ver y Editar Listado"))
        self.buttonViewTree.setText(_translate("Dialog", "Visualización del Árbol"))
        self.buttonAbout.setText(_translate("Dialog", "Acerca de"))
        self.labelMoviesInTotal.setText(_translate("Dialog", "Películas en Total"))
        self.labelNumberOfMovies.setText(_translate("Dialog", "<html><head/><body><p>%s</p></body></html>" % self.movieList.getTotalItems()))



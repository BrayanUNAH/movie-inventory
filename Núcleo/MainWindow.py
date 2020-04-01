# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Núcleo.AddWindow import AddWindow
from Núcleo.EditWindow import EditWindow
from Núcleo.LinkedList import LinkedList
from Núcleo.Movie import Movie
from Núcleo.MemoryManager import MemoryManager
from Núcleo.AboutWindow import AboutWindow
import os


class MainWindow(object):

    def __init__(self):
        self.memory = MemoryManager()
        if os.path.isfile('memory\\memory.json'):
            self.movieList = self.memory.loadLinkedList() 
        else:
            self.movieList = LinkedList()

    def closeEvent(self, event):
        self.memory.saveLinkedList(self.movieList, self.movieList.getTotalItems())


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(388, 544)
        self.buttonAddMovie = QtWidgets.QPushButton(Dialog)
        self.buttonAddMovie.setGeometry(QtCore.QRect(80, 300, 221, 61))
        self.buttonAddMovie.setObjectName("buttonAddMovie")
        self.buttonEditList = QtWidgets.QPushButton(Dialog)
        self.buttonEditList.setGeometry(QtCore.QRect(80, 380, 221, 61))
        self.buttonEditList.setObjectName("buttonEditList")
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
        self.buttonEditList.clicked.connect(self.editWindow)
        self.buttonViewTree.clicked.connect(self.viewTree)
        self.buttonAbout.clicked.connect(self.aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def addWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddWindow(self.movieList)
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.buttonAdd.clicked.connect(self.updateLabelNumberOfMovies)
        

    def editWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = EditWindow(self.movieList)
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.buttonDeleteItem.clicked.connect(self.updateLabelNumberOfMovies)
        

    def updateLabelNumberOfMovies(self):
        self.labelNumberOfMovies.setText(("<html><head/><body><p>%s</p></body></html>" % self.movieList.getTotalItems()))

    def viewTree(self):
        self.movieList.drawBinaryTreeDuration()

    def aboutWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ventana Principal"))
        self.buttonAddMovie.setText(_translate("Dialog", "Agregar"))
        self.buttonEditList.setText(_translate("Dialog", "Ver y Editar Listado"))
        self.buttonViewTree.setText(_translate("Dialog", "Visualización del Árbol"))
        self.buttonAbout.setText(_translate("Dialog", "Acerca de"))
        self.labelMoviesInTotal.setText(_translate("Dialog", "Películas en Total"))
        self.updateLabelNumberOfMovies()


# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from LinkedList import LinkedList
from AddWindow import AddWindow
from Movie import Movie

class EditWindow(object):

    def __init__(self, movieList):
        self.movieList = movieList

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 366)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 611, 171))
        self.treeWidget.setObjectName("treeWidget")
        for i in range(self.movieList.getTotalItems()):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.labelItemNumber = QtWidgets.QLabel(Dialog)
        self.labelItemNumber.setGeometry(QtCore.QRect(100, 220, 151, 20))
        self.labelItemNumber.setObjectName("labelItemNumber")
        self.textItemNumber = QtWidgets.QPlainTextEdit(Dialog)
        self.textItemNumber.setGeometry(QtCore.QRect(130, 250, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.textItemNumber.setFont(font)
        self.textItemNumber.setPlainText("")
        self.textItemNumber.setObjectName("textItemNumber")
        self.buttonEditItem = QtWidgets.QPushButton(Dialog)
        self.buttonEditItem.setGeometry(QtCore.QRect(290, 250, 81, 61))
        self.buttonEditItem.setObjectName("buttonEditItem")
        self.buttonDeleteItem = QtWidgets.QPushButton(Dialog)
        self.buttonDeleteItem.setGeometry(QtCore.QRect(410, 250, 81, 61))
        self.buttonDeleteItem.setObjectName("buttonDeleteItem")
        self.buttonEditItem.clicked.connect(self.editItem)
        self.buttonDeleteItem.clicked.connect(self.deleteItem)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def editItem(self):
        try:
            itemNumber = int(self.textItemNumber.toPlainText())
        except ValueError:
            self.invalidMessage()
            return False
        if itemNumber < self.movieList.getTotalItems() and itemNumber >= 0:
            self.addWindow(self.movieList.search(itemNumber), itemNumber)
        else:
            self.invalidMessage()
        return True

    def invalidMessage(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle("No válido")
        self.message.setText("Número de Item no válido")
        x = self.message.exec_()


    def addWindow(self, movie, itemNumber):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddWindow(self.movieList)
        self.ui.setupUi(self.window)

        self.ui.textNameMovie.setPlainText(movie.value.getMovieName())
        self.ui.textDurationTime.setPlainText(movie.value.getMovieDuration())
        self.ui.textDirector.setPlainText(movie.value.getDirectorName())
        self.ui.textDescription.setPlainText(movie.value.getDescription())

        self.ui.buttonAdd.hide()
        
        self.ui.auxButtonAdd = QtWidgets.QPushButton(self.window)
        self.ui.auxButtonAdd.setGeometry(QtCore.QRect(374, 440, 101, 41))
        self.ui.auxButtonAdd.setObjectName("auxButtonAdd")
        self.ui.auxButtonAdd.setText("Agregar")
        self.window.show()
        self.OverwriteMovie(itemNumber)
        self.ui.auxButtonAdd.clicked.connect(self.ui.clearTextBox)

    def OverwriteMovie(self, itemNumber):
        movieName = self.ui.textNameMovie.toPlainText()
        movieDuration = self.ui.textDurationTime.toPlainText()
        directorName = self.ui.textDirector.toPlainText()
        category = self.ui.category.currentText()
        description = self.ui.textDescription.toPlainText()

        if movieName == "" or movieDuration == "" or directorName == "" or directorName == "" or category == "" or description == "":
            self.message = QtWidgets.QMessageBox()
            self.message.setWindowTitle("Incompleto")
            self.message.setText("Todos los campos deben estar completos")
            x = self.message.exec_()
            return False
        movie = Movie(movieName, movieDuration,
                      directorName, category, description)
        self.movieList.overwrite(itemNumber, movie)
        return True


    def deleteItem(self):
        try:
            itemNumber = int(self.textItemNumber.toPlainText())
        except ValueError:
            self.invalidMessage()
            return False
        if itemNumber < self.movieList.getTotalItems() and itemNumber >= 0:
            self.movieList.remove(itemNumber)
        else:
            self.invalidMessage()
        return True


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ventana Editar"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "No. Item"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Nombre"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "Duración"))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "Descripción"))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "Director"))
        self.treeWidget.headerItem().setText(5, _translate("Dialog", "Categoría"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        for i in range (self.movieList.getTotalItems()):
            for y in range(0,6):
                    self.treeWidget.topLevelItem(i).setText(y, _translate("Dialog", "%s" % self.movieList.getTotalItems()))
        """self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "Item"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("Dialog", "nombre"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("Dialog", "duración"))
        self.treeWidget.topLevelItem(0).setText(3, _translate("Dialog", "descripción esto es una description"))
        self.treeWidget.topLevelItem(0).setText(4, _translate("Dialog", "director"))
        self.treeWidget.topLevelItem(0).setText(5, _translate("Dialog", "categoría"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog", "sd"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("Dialog", "1"))
        self.treeWidget.topLevelItem(1).setText(2, _translate("Dialog", "sd"))
        self.treeWidget.topLevelItem(1).setText(3, _translate("Dialog", "sd"))
        self.treeWidget.topLevelItem(1).setText(4, _translate("Dialog", "sd"))
        self.treeWidget.topLevelItem(1).setText(5, _translate("Dialog", "sd"))"""
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.labelItemNumber.setText(_translate("Dialog", "No. de Item a Editar o Eliminar"))
        self.buttonEditItem.setText(_translate("Dialog", "Editar"))
        self.buttonDeleteItem.setText(_translate("Dialog", "Borrar"))

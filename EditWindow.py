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
        self.movieTable = QtWidgets.QTreeWidget(Dialog)
        self.movieTable.setGeometry(QtCore.QRect(20, 20, 611, 171))
        self.movieTable.setObjectName("movieTable")
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
        self.buttonDeleteItem.clicked.connect(self.updateMovieTable)
        self.retranslateUi(Dialog)
        self.updateMovieTable()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def updateMovieTable(self):
        self.movieTable.clear()

        for i in range(self.movieList.getTotalItems()):
            item = QtWidgets.QTreeWidgetItem(self.movieTable)

        for row in range (self.movieList.getTotalItems()):
            for column in range(0, 6):
                    self.movieTable.topLevelItem(row).setText(column, "%s" % self.movieList.getTotalItems())


    def editItem(self):
        try:
            itemNumber = int(self.textItemNumber.toPlainText())
        except ValueError:
            self.invalidMessage()
            return False
        if itemNumber < self.movieList.getTotalItems() and itemNumber >= 0:
            self.addWindow(self.movieList.search(itemNumber))
        else:
            self.invalidMessage()
        return True

    def invalidMessage(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle("No válido")
        self.message.setText("Número de Item no válido")
        x = self.message.exec_()


    def addWindow(self, movie):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddWindow(self.movieList)
        self.ui.setupUi(self.window)

        self.ui.textNameMovie.setPlainText(movie.value.getMovieName())
        self.ui.textDurationTime.setPlainText(movie.value.getMovieDuration())
        self.ui.textDirector.setPlainText(movie.value.getDirectorName())
        self.ui.textDescription.setPlainText(movie.value.getDescription())
        self.ui.buttonAdd.clicked.connect(self.window.close)
        self.ui.buttonAdd.clicked.connect(self.overwriteMovie)
        self.window.show()


    def overwriteMovie(self):
        itemNumber = int(self.textItemNumber.toPlainText())
        lastMovie = self.movieList.getTotalItems()-1
        movieToInsert = self.movieList.search(lastMovie).value
        self.movieList.remove(lastMovie)
        self.movieList.overwrite(itemNumber, movieToInsert)
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
        self.movieTable.headerItem().setText(0, _translate("Dialog", "No. Item"))
        self.movieTable.headerItem().setText(1, _translate("Dialog", "Nombre"))
        self.movieTable.headerItem().setText(2, _translate("Dialog", "Duración"))
        self.movieTable.headerItem().setText(3, _translate("Dialog", "Descripción"))
        self.movieTable.headerItem().setText(4, _translate("Dialog", "Director"))
        self.movieTable.headerItem().setText(5, _translate("Dialog", "Categoría"))
        __sortingEnabled = self.movieTable.isSortingEnabled()
        self.movieTable.setSortingEnabled(False)
        self.movieTable.setSortingEnabled(__sortingEnabled)
        self.labelItemNumber.setText(_translate("Dialog", "No. de Item a Editar o Eliminar"))
        self.buttonEditItem.setText(_translate("Dialog", "Editar"))
        self.buttonDeleteItem.setText(_translate("Dialog", "Borrar"))
        


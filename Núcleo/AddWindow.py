# -*- coding: utf-8 -*-
from Núcleo.Movie import Movie
from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
from Núcleo.ConfirmationWindow import ConfirmationWindow

class AddWindow(object):

    def __init__(self, movieList):
        self.movieList = movieList

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(697, 501)
        Dialog.setAccessibleName("")
        Dialog.setAccessibleDescription("")
        self.category = QtWidgets.QComboBox(Dialog)
        self.category.setGeometry(QtCore.QRect(30, 390, 641, 22))
        self.category.setObjectName("category")
        for itemCategory in range (31):
            self.category.addItem("")
        self.labelNameMovie = QtWidgets.QLabel(Dialog)
        self.labelNameMovie.setGeometry(QtCore.QRect(30, 20, 131, 20))
        self.labelNameMovie.setObjectName("labelNameMovie")
        self.labelMovieDuration = QtWidgets.QLabel(Dialog)
        self.labelMovieDuration.setGeometry(QtCore.QRect(30, 100, 431, 16))
        self.labelMovieDuration.setObjectName("labelMovieDuration")
        self.labelDescription = QtWidgets.QLabel(Dialog)
        self.labelDescription.setGeometry(QtCore.QRect(30, 170, 281, 16))
        self.labelDescription.setObjectName("labelDescription")
        self.labelDirector = QtWidgets.QLabel(Dialog)
        self.labelDirector.setGeometry(QtCore.QRect(30, 300, 171, 16))
        self.labelDirector.setObjectName("labelDirector")
        self.labelCategory = QtWidgets.QLabel(Dialog)
        self.labelCategory.setGeometry(QtCore.QRect(30, 370, 131, 16))
        self.labelCategory.setObjectName("labelCategory")
        self.buttonDelete = QtWidgets.QPushButton(Dialog)
        self.buttonDelete.setGeometry(QtCore.QRect(204, 440, 91, 41))
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonAdd = QtWidgets.QPushButton(Dialog)
        self.buttonAdd.setGeometry(QtCore.QRect(374, 440, 101, 41))
        self.buttonAdd.setObjectName("buttonAdd")
        self.textDescription = QtWidgets.QPlainTextEdit(Dialog)
        self.textDescription.setGeometry(QtCore.QRect(30, 190, 641, 91))
        self.textDescription.setPlainText("")
        self.textDescription.setObjectName("textDescription")
        self.textNameMovie = QtWidgets.QPlainTextEdit(Dialog)
        self.textNameMovie.setGeometry(QtCore.QRect(30, 40, 641, 41))
        self.textNameMovie.setPlainText("")
        self.textNameMovie.setObjectName("textNameMovie")
        self.textDurationTime = QtWidgets.QPlainTextEdit(Dialog)
        self.textDurationTime.setGeometry(QtCore.QRect(30, 120, 641, 31))
        self.textDurationTime.setPlainText("")
        self.textDurationTime.setObjectName("textDurationTime")
        self.textDirector = QtWidgets.QPlainTextEdit(Dialog)
        self.textDirector.setGeometry(QtCore.QRect(30, 320, 641, 31))
        self.textDirector.setPlainText("")
        self.textDirector.setObjectName("textDirector")
        self.retranslateUi(Dialog)
        self.buttonDelete.clicked.connect(self.confirmationMessage)
        self.retranslateUi(Dialog)
        self.buttonAdd.clicked.connect(self.addToLinkedList)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def confirmationMessage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ConfirmationWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.buttonOK.clicked.connect(self.clearTextBox)
        self.ui.buttonOK.clicked.connect(self.window.close)
        self.ui.buttonCancel.clicked.connect(self.window.close)
        

    def addToLinkedList(self):
        movieName = self.textNameMovie.toPlainText()
        movieDuration = self.textDurationTime.toPlainText()
        directorName = self.textDirector.toPlainText()
        category = self.category.currentText()
        description = self.textDescription.toPlainText()
        if (movieName == "" or movieDuration == "" or directorName == "" or directorName == "" or category == "Seleccionar una categoría" or description == ""):
            self.incompleteMessage()
            return False
        if self.checkErrorMovieDuration(movieDuration):
            self.movieDurationErrorMessage()
            return False
        movieDuration = "%s" % self.toSeconds(movieDuration)
        movie = Movie(movieName, movieDuration, directorName, category, description)
        self.movieList.push(movie)
        self.clearTextBox()
        return True

    def checkErrorMovieDuration(self, movieDuration):
        movieDuration = movieDuration.split(':')
        if len(movieDuration) == 3:
            for i in range(len(movieDuration)):
                try:
                    checkInt = int(movieDuration[i])
                except ValueError as identifier:
                    return True
        else:
            return True
        return False
    

    def movieDurationErrorMessage(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle("Error")
        self.message.setText("El formato de la duración es incorrecto")
        x = self.message.exec_()


    def toSeconds(self, durationTime):
        durationTime = durationTime.split(':')
        hours = int(durationTime[0])
        minutes = int(durationTime[1])
        seconds = int(durationTime[2])

        totalSeconds = hours*3600 + minutes*60 + seconds
        return totalSeconds

    def incompleteMessage(self):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle("Incompleto")
        self.message.setText("Todos los campos deben estar completos")
        x = self.message.exec_()

    def clearTextBox(self):
        self.textNameMovie.clear()
        self.textDurationTime.clear()
        self.textDirector.clear()
        self.textDescription.clear()
        self.category.setCurrentText(("Seleccionar una categoría"))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Agregar"))
        self.labelNameMovie.setText(_translate("Dialog", "Nombre de la Película"))
        self.labelMovieDuration.setText(_translate("Dialog", "Duración de la Película (HH:MM:SS)"))
        self.labelDescription.setText(_translate("Dialog", "Descripción"))
        self.labelDirector.setText(_translate("Dialog", "Director"))
        self.labelCategory.setText(_translate("Dialog", "Categoría"))
        self.buttonDelete.setText(_translate("Dialog", "Borrar"))
        self.buttonAdd.setText(_translate("Dialog", "Agregar"))

        self.category.setItemText(0, _translate("Dialog", "Seleccionar una categoría"))
        self.category.setItemText(1, _translate("Dialog", "Comedia"))
        self.category.setItemText(2, _translate("Dialog", "Musical"))
        self.category.setItemText(3, _translate("Dialog", "Documental"))
        self.category.setItemText(4, _translate("Dialog", "Hechos Reales"))
        self.category.setItemText(5, _translate("Dialog", "Acción"))
        self.category.setItemText(6, _translate("Dialog", "Artes Marciales"))
        self.category.setItemText(7, _translate("Dialog", "Aventuras"))
        self.category.setItemText(8, _translate("Dialog", "Ciencia Ficción"))
        self.category.setItemText(9, _translate("Dialog", "Animación"))
        self.category.setItemText(10, _translate("Dialog", "Espadas y Hechicería"))
        self.category.setItemText(11, _translate("Dialog", "Espionaje"))
        self.category.setItemText(12, _translate("Dialog", "Horror"))
        self.category.setItemText(13, _translate("Dialog", "Misterio"))
        self.category.setItemText(14, _translate("Dialog", "Muertos Vivientes"))
        self.category.setItemText(15, _translate("Dialog", "Propaganda"))
        self.category.setItemText(16, _translate("Dialog", "Suspenso"))
        self.category.setItemText(17, _translate("Dialog", "Terror"))
        self.category.setItemText(18, _translate("Dialog", "Deportivas"))
        self.category.setItemText(19, _translate("Dialog", "Dramáticas"))
        self.category.setItemText(20, _translate("Dialog", "Fantásticas"))
        self.category.setItemText(21, _translate("Dialog", "Infantiles"))
        self.category.setItemText(22, _translate("Dialog", "Policíacas"))
        self.category.setItemText(23, _translate("Dialog", "Psicológicas"))
        self.category.setItemText(24, _translate("Dialog", "Románticas"))
        self.category.setItemText(25, _translate("Dialog", "Sobre Animales"))
        self.category.setItemText(26, _translate("Dialog", "Sobre Aviación"))
        self.category.setItemText(27, _translate("Dialog", "Sobre Delincuencia"))
        self.category.setItemText(28, _translate("Dialog", "Sobre Discapacitados"))
        self.category.setItemText(29, _translate("Dialog", "Sobre Religión"))
        self.category.setItemText(30, _translate("Dialog", "Sobre Política"))


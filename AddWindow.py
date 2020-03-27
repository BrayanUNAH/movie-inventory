# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class AddWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(697, 501)
        Dialog.setAccessibleName("")
        Dialog.setAccessibleDescription("")
        self.category = QtWidgets.QComboBox(Dialog)
        self.category.setGeometry(QtCore.QRect(30, 390, 641, 22))
        self.category.setObjectName("category")
        self.category.addItem("")
        self.category.addItem("")
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
        self.buttonDelete.clicked.connect(self.textNameMovie.clear)
        self.buttonDelete.clicked.connect(self.textDurationTime.clear)
        self.buttonDelete.clicked.connect(self.textDescription.clear)
        self.buttonDelete.clicked.connect(self.textDirector.clear)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Agregar"))
        self.category.setItemText(0, _translate("Dialog", "Comedia"))
        self.category.setItemText(1, _translate("Dialog", "Musical"))
        self.category.setItemText(2, _translate("Dialog", "Documental"))
        self.labelNameMovie.setText(_translate("Dialog", "Nombre de la Película"))
        self.labelMovieDuration.setText(_translate("Dialog", "Duración de la Película (HH:MM:SS)"))
        self.labelDescription.setText(_translate("Dialog", "Descripción"))
        self.labelDirector.setText(_translate("Dialog", "Director"))
        self.labelCategory.setText(_translate("Dialog", "Categoría"))
        self.buttonDelete.setText(_translate("Dialog", "Borrar"))
        self.buttonAdd.setText(_translate("Dialog", "Agregar"))

    

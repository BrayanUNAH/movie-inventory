# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class ConfirmationWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(209, 121)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 29, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.buttonOK = QtWidgets.QPushButton(Dialog)
        self.buttonOK.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.buttonOK.setObjectName("buttonOK")
        self.buttonCancel = QtWidgets.QPushButton(Dialog)
        self.buttonCancel.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.buttonCancel.setObjectName("buttonCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "¿Está seguro?"))
        self.buttonOK.setText(_translate("Dialog", "Ok"))
        self.buttonCancel.setText(_translate("Dialog", "Cancelar"))

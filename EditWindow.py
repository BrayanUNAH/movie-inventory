# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class EditWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 366)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 611, 171))
        self.treeWidget.setObjectName("treeWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 220, 151, 20))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 250, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 81, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 250, 81, 61))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "No. Item"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Nombre"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "Duración"))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "Descripción"))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "Director"))
        self.treeWidget.headerItem().setText(5, _translate("Dialog", "Categoría"))
        self.label.setText(_translate("Dialog", "No. de Item a Editar o Eliminar"))
        self.pushButton.setText(_translate("Dialog", "Editar"))
        self.pushButton_2.setText(_translate("Dialog", "Borrar"))

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class EditWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(653, 366)
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(20, 20, 611, 171))
        self.treeWidget.setObjectName("treeWidget")
        for i in range(2):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.labelItemNumber = QtWidgets.QLabel(Dialog)
        self.labelItemNumber.setGeometry(QtCore.QRect(100, 220, 151, 20))
        self.labelItemNumber.setObjectName("labelItemNumber")
        self.textItemNumber = QtWidgets.QPlainTextEdit(Dialog)
        self.textItemNumber.setGeometry(QtCore.QRect(130, 250, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.textItemNumber.setFont(font)
        self.textItemNumber.setPlainText("d")
        self.textItemNumber.setObjectName("textItemNumber")
        self.buttonEditItem = QtWidgets.QPushButton(Dialog)
        self.buttonEditItem.setGeometry(QtCore.QRect(290, 250, 81, 61))
        self.buttonEditItem.setObjectName("buttonEditItem")
        self.buttonDeleteItem = QtWidgets.QPushButton(Dialog)
        self.buttonDeleteItem.setGeometry(QtCore.QRect(410, 250, 81, 61))
        self.buttonDeleteItem.setObjectName("buttonDeleteItem")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "Item"))
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
        self.treeWidget.topLevelItem(1).setText(5, _translate("Dialog", "sd"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.labelItemNumber.setText(_translate("Dialog", "No. de Item a Editar o Eliminar"))
        self.buttonEditItem.setText(_translate("Dialog", "Editar"))
        self.buttonDeleteItem.setText(_translate("Dialog", "Borrar"))

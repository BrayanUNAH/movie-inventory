# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class AboutWindow(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(442, 491)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/glasses-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(about)
        self.label.setGeometry(QtCore.QRect(100, 0, 221, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/logos-UNAH-11.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(about)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 191, 231))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "Acerca De"))
        self.label_2.setText(_translate("about", "UNAH\n"
"Algoritmos Y Estructuras de Datos\n"
"Sección: 0900\n"
"I PAC 2020\n"
"Catedrático: Ing. José Inestroza\n"
"\n"
"\n"
"\n"
"Integrantes:                     No Cuenta:\n"
"David Raudales              20181005992                          \n"
"Luis Espinal                     20181001150\n"
"Bryan Medina                 20181005502\n"
"Brayan Medina               20181002691"))

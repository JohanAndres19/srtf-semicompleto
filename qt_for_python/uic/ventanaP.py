# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\usuario\OneDrive\Documentos\semestre 2021-3\sistemas operativos\Algoritmo FCFS\AlgoritmoPython\ventanaP.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qt_for_python.rcc.source import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 604)
        MainWindow.setStyleSheet("*{\n"
" \n"
"    font-family: Comic Sans Ms;\n"
"    background-image:url(:/imagenes/imagenes/HD-wallpaper-abstract-colorful-colors-pattern-thumbnail.jpg);\n"
"}\n"
"\n"
"QPushButton{\n"
"   background:#2d89ef;\n"
"   color: white;\n"
"   border: 2px solid;\n"
"   border-radius:15px;\n"
"   font-size:15px;        \n"
"}\n"
"\n"
"QFrame{\n"
"    /*background: rgb(0, 0, 0) transparent;\n"
"    border:transparent;*/\n"
"}\n"
"\n"
"QTableView {\n"
"    color: white;\n"
"    font-size:14px;\n"
"    background: rgb(59, 89, 213);\n"
"   border: 2px solid;\n"
"   border-radius:15px;\n"
"   \n"
"}\n"
"\n"
"\n"
"QHeaderView{\n"
"  qproperty-defaultAlignment: AlignHCenter;\n"
"  background: rgb(59, 89, 213);\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QComboBox{\n"
"   background:#2d89ef;\n"
"   color: white;\n"
"   border: 2px solid;\n"
"   border-radius:15px;\n"
"   font-size:15px;        \n"
"}\n"
"\n"
"QLabel{\n"
"    background: rgb(0, 0, 0) transparent;    \n"
"    color:white;\n"
"    font-weight: 900;\n"
"     font-size:18px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_bloquear = QtWidgets.QPushButton(self.centralwidget)
        self.boton_bloquear.setGeometry(QtCore.QRect(950, 30, 75, 31))
        self.boton_bloquear.setObjectName("boton_bloquear")
        self.boton_simular = QtWidgets.QPushButton(self.centralwidget)
        self.boton_simular.setGeometry(QtCore.QRect(770, 30, 75, 31))
        self.boton_simular.setObjectName("boton_simular")
        self.boton_agregar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_agregar.setGeometry(QtCore.QRect(580, 30, 81, 31))
        self.boton_agregar.setObjectName("boton_agregar")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(560, 70, 501, 221))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 501, 221))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 70, 491, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 1, 491, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 300, 1021, 291))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 30, 171, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 121, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_bloquear.setText(_translate("MainWindow", "Bloquear"))
        self.boton_simular.setText(_translate("MainWindow", "Simular"))
        self.boton_agregar.setText(_translate("MainWindow", "Agregar"))
        self.label.setText(_translate("MainWindow", "ALGORITMO"))


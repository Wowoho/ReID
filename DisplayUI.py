# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(20, 10, 1050, 680))
        self.gridWidget.setObjectName("gridWidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gridWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(750, 40, 300, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.gridWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 640, 480))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DisplayLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.DisplayLabel.setGeometry(QtCore.QRect(0, 0, 781, 491))
        self.DisplayLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.DisplayLabel.setText("")
        self.DisplayLabel.setObjectName("DisplayLabel")
        self.verticalLayout_2.addWidget(self.DisplayLabel)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.gridWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 530, 381, 60))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButtonCam = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButtonCam.setObjectName("radioButtonCam")
        self.horizontalLayout_5.addWidget(self.radioButtonCam)
        self.radioButtonFile = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButtonFile.setObjectName("radioButtonFile")
        self.horizontalLayout_5.addWidget(self.radioButtonFile)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.gridWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 590, 381, 60))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Open = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Open.setObjectName("Open")
        self.horizontalLayout.addWidget(self.Open)
        self.Close = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Close.setObjectName("Close")
        self.horizontalLayout.addWidget(self.Close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.radioButtonCam.setText(_translate("MainWindow", "Camera"))
        self.radioButtonFile.setText(_translate("MainWindow", "Load File"))


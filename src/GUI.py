# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 90, 731, 521))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_ImageShow = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_ImageShow.setContentsMargins(0, 0, 0, 0)
        self.layout_ImageShow.setObjectName("layout_ImageShow")
        self.graphicsView_Image = QtWidgets.QGraphicsView(self.verticalLayoutWidget_2)
        self.graphicsView_Image.setObjectName("graphicsView_Image")
        self.layout_ImageShow.addWidget(self.graphicsView_Image)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_ModelTraining = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_ModelTraining.setContentsMargins(0, 0, 0, 0)
        self.layout_ModelTraining.setObjectName("layout_ModelTraining")
        self.label_TrainModel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_TrainModel.setObjectName("label_TrainModel")
        self.layout_ModelTraining.addWidget(self.label_TrainModel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 610, 901, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layout_RecognOutput = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_RecognOutput.setContentsMargins(0, 0, 0, 0)
        self.layout_RecognOutput.setObjectName("layout_RecognOutput")
        self.label_RecognOutput = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_RecognOutput.setObjectName("label_RecognOutput")
        self.layout_RecognOutput.addWidget(self.label_RecognOutput)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(730, 90, 171, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_LoadRecogn = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_LoadRecogn.setContentsMargins(0, 0, 0, 0)
        self.layout_LoadRecogn.setObjectName("layout_LoadRecogn")
        self.button_LoadImage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_LoadImage.setObjectName("button_LoadImage")
        self.layout_LoadRecogn.addWidget(self.button_LoadImage)
        self.button_Recogn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_Recogn.setObjectName("button_Recogn")
        self.layout_LoadRecogn.addWidget(self.button_Recogn)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image-Analysis-Detecting-car-models"))
        self.label_TrainModel.setText(_translate("MainWindow", ""))
        self.label_RecognOutput.setText(_translate("MainWindow", ""))
        self.button_LoadImage.setText(_translate("MainWindow", "Load Image"))
        self.button_Recogn.setText(_translate("MainWindow", "Categorize Image"))


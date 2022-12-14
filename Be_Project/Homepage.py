# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from RealDataset import Ui_RealDatasetWindow
from TrainDataset import Ui_TrainDatasetWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groups_2 = QtWidgets.QPushButton(self.centralwidget)
        self.groups_2.setGeometry(QtCore.QRect(30, 120, 131, 31))
        self.groups_2.setObjectName("groups_2")
        self.groups_3 = QtWidgets.QPushButton(self.centralwidget)
        self.groups_3.setGeometry(QtCore.QRect(30, 160, 81, 31))
        self.groups_3.setStyleSheet("background-color: rgb(110, 255, 127);")
        self.groups_3.setObjectName("groups_3")
        self.groups_4 = QtWidgets.QPushButton(self.centralwidget)
        self.groups_4.setGeometry(QtCore.QRect(30, 210, 131, 31))
        self.groups_4.setObjectName("groups_4")
        self.groups_6 = QtWidgets.QPushButton(self.centralwidget)
        self.groups_6.setGeometry(QtCore.QRect(150, 320, 131, 31))
        self.groups_6.setStyleSheet("background-color: rgb(12, 255, 32);")
        self.groups_6.setObjectName("groups_6")
        self.groups_7 = QtWidgets.QPushButton(self.centralwidget)
        self.groups_7.setGeometry(QtCore.QRect(280, 210, 131, 31))
        self.groups_7.setObjectName("groups_7")
        self.groups_8 = QtWidgets.QPushButton(self.centralwidget)
        self.groups_8.setGeometry(QtCore.QRect(280, 120, 131, 31))
        self.groups_8.setObjectName("groups_8")
        self.groups_9 = QtWidgets.QPushButton(self.centralwidget)
        self.groups_9.setGeometry(QtCore.QRect(30, 250, 81, 31))
        self.groups_9.setStyleSheet("background-color: rgb(110, 255, 127);")
        self.groups_9.setObjectName("groups_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # button click events

        self.groups_2.clicked.connect(self.openUploadDataset)
        self.groups_4.clicked.connect(self.openUploadDataset)

        self.groups_7.clicked.connect(self.openRealDataset)
        self.groups_8.clicked.connect(self.openTrainDataset)

        # button click events over

    # open browse file dialog box
    def openUploadDataset(self):
        file_name = QFileDialog.getOpenFileNames()
        print(file_name)

    # open RealDataset.ui
    def openRealDataset(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RealDatasetWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # open TrainDataset.ui
    def openTrainDataset(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TrainDatasetWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Home Page"))
        self.groups_2.setText(_translate("MainWindow", "Upload Dataset"))
        self.groups_3.setText(_translate("MainWindow", "Run model"))
        self.groups_4.setText(_translate("MainWindow", "Upload Real Dataset"))
        self.groups_6.setText(_translate("MainWindow", "Result"))
        self.groups_7.setText(_translate("MainWindow", "View Dataset"))
        self.groups_8.setText(_translate("MainWindow", "View Dataset"))
        self.groups_9.setText(_translate("MainWindow", "Run model"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

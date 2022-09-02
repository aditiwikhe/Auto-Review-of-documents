# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LabelFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LabelFileWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filename_label = QtWidgets.QLabel(self.centralwidget)
        self.filename_label.setGeometry(QtCore.QRect(20, 40, 411, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.filename_label.setFont(font)
        self.filename_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filename_label.setObjectName("filename_label")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(50, 290, 71, 31))
        self.add_btn.setStyleSheet("background-color: rgb(88, 138, 255);")
        self.add_btn.setObjectName("add_btn")
        self.extracted_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.extracted_dropdown.setGeometry(QtCore.QRect(50, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.extracted_dropdown.setFont(font)
        self.extracted_dropdown.setStyleSheet("")
        self.extracted_dropdown.setObjectName("extracted_dropdown")
        self.extracted_dropdown.addItem("")
        self.extracted_dropdown.addItem("")
        self.extracted_dropdown.addItem("")
        self.extracted_dropdown.addItem("")
        self.extracted_label = QtWidgets.QLabel(self.centralwidget)
        self.extracted_label.setGeometry(QtCore.QRect(50, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.extracted_label.setFont(font)
        self.extracted_label.setObjectName("extracted_label")
        self.new_label = QtWidgets.QLabel(self.centralwidget)
        self.new_label.setGeometry(QtCore.QRect(50, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_label.setFont(font)
        self.new_label.setObjectName("new_label")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(252, 350, 161, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.newLabel_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.newLabel_txt.setGeometry(QtCore.QRect(50, 240, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.newLabel_txt.setFont(font)
        self.newLabel_txt.setPlainText("")
        self.newLabel_txt.setObjectName("newLabel_txt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filename_label.setText(_translate("MainWindow", "File Name"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.extracted_dropdown.setItemText(0, _translate("MainWindow", "Label 1"))
        self.extracted_dropdown.setItemText(1, _translate("MainWindow", "Label 2"))
        self.extracted_dropdown.setItemText(2, _translate("MainWindow", "Label 3"))
        self.extracted_dropdown.setItemText(3, _translate("MainWindow", "Label 4"))
        self.extracted_label.setText(_translate("MainWindow", "Extracted labels"))
        self.new_label.setText(_translate("MainWindow", "Add new label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LabelFileWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

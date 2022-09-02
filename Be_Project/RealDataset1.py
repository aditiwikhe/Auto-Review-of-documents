# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RealDataset.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PdfViewer import PdfViewer
from LabelFile import Ui_LabelFileWindow


class Ui_RealDatasetWindow(object):
    def setupUi(self, MainWindow, client):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(30, 20, 421, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        # self.view_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.view_btn.setGeometry(QtCore.QRect(270, 130, 81, 31))
        # self.view_btn.setObjectName("view_btn")
        # self.startline = QtWidgets.QFrame(self.centralwidget)
        # self.startline.setGeometry(QtCore.QRect(30, 110, 411, 21))
        # self.startline.setFrameShape(QtWidgets.QFrame.HLine)
        # self.startline.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.startline.setObjectName("startline")
        # self.filename_label = QtWidgets.QLabel(self.centralwidget)
        # self.filename_label.setGeometry(QtCore.QRect(30, 140, 141, 16))
        # self.filename_label.setObjectName("filename_label")
        # self.groups_10 = QtWidgets.QPushButton(self.centralwidget)
        # self.groups_10.setGeometry(QtCore.QRect(270, 180, 81, 31))
        # self.groups_10.setObjectName("groups_10")
        # self.line_2 = QtWidgets.QFrame(self.centralwidget)
        # self.line_2.setGeometry(QtCore.QRect(30, 160, 411, 21))
        # self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_2.setObjectName("line_2")
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(30, 190, 141, 16))
        # self.label_4.setObjectName("label_4")
        # self.groups_11 = QtWidgets.QPushButton(self.centralwidget)
        # self.groups_11.setGeometry(QtCore.QRect(270, 230, 81, 31))
        # self.groups_11.setObjectName("groups_11")
        # self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(30, 240, 141, 16))
        # self.label_5.setObjectName("label_5")
        # self.line_3 = QtWidgets.QFrame(self.centralwidget)
        # self.line_3.setGeometry(QtCore.QRect(30, 210, 411, 21))
        # self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_3.setObjectName("line_3")
        # self.groups_12 = QtWidgets.QPushButton(self.centralwidget)
        # self.groups_12.setGeometry(QtCore.QRect(270, 280, 81, 31))
        # self.groups_12.setObjectName("groups_12")
        # self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(30, 290, 141, 16))
        # self.label_6.setObjectName("label_6")
        # self.line_4 = QtWidgets.QFrame(self.centralwidget)
        # self.line_4.setGeometry(QtCore.QRect(30, 260, 411, 21))
        # self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_4.setObjectName("line_4")
        self.endline = QtWidgets.QFrame(self.centralwidget)
        self.endline.setGeometry(QtCore.QRect(30, 360, 411, 21))
        self.endline.setFrameShape(QtWidgets.QFrame.HLine)
        self.endline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.endline.setObjectName("endline")
        # self.labelfile_btn = QtWidgets.QPushButton(self.centralwidget)
        # self.labelfile_btn.setGeometry(QtCore.QRect(360, 130, 81, 31))
        # self.labelfile_btn.setObjectName("labelfile_btn")
        # self.groups_13 = QtWidgets.QPushButton(self.centralwidget)
        # self.groups_13.setGeometry(QtCore.QRect(360, 180, 81, 31))
        # self.groups_13.setObjectName("groups_13")
        # self.groups_14 = QtWidgets.QPushButton(self.centralwidget)
        # self.groups_14.setGeometry(QtCore.QRect(360, 230, 81, 31))
        # self.groups_14.setObjectName("groups_14")
        # self.groups_15 = QtWidgets.QPushButton(self.centralwidget)
        # self.groups_15.setGeometry(QtCore.QRect(360, 280, 81, 31))
        # self.groups_15.setObjectName("groups_15")
        self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.submit_btn.setGeometry(QtCore.QRect(30, 440, 81, 31))
        self.submit_btn.setStyleSheet("background-color: rgb(88, 138, 255);")
        self.submit_btn.setObjectName("submit_btn")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(280, 450, 161, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # search box
        self.search_txt_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_txt_1.setGeometry(QtCore.QRect(30, 80, 191, 31))
        self.search_txt_1.setPlaceholderText("Search by name")
        # self.search_txt_1.setAlignment(QtCore.Qt.AlignLeft)
        self.search_txt_1.setObjectName("search_txt_1")
        self.search_btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn_1.setGeometry(QtCore.QRect(170, 80, 51, 31))
        self.search_btn_1.setStyleSheet("\n"
                                        "border-color: rgb(255, 0, 0);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "font: 75 10pt \"MS Shell Dlg 2\";")
        self.search_btn_1.setObjectName("search_btn_1")
        self.search_txt_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.search_txt_2.setGeometry(QtCore.QRect(250, 80, 191, 31))
        self.search_txt_2.setPlaceholderText("Search by category")
        # self.search_txt_2.setAlignment(QtCore.Qt.AlignLeft)
        self.search_txt_2.setObjectName("search_txt_2")
        self.search_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn_2.setGeometry(QtCore.QRect(390, 80, 51, 31))
        self.search_btn_2.setStyleSheet("\n"
                                        "border-color: rgb(255, 0, 0);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "font: 75 10pt \"MS Shell Dlg 2\";")
        self.search_btn_2.setObjectName("search_btn_2")
        self.search_cancel_btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.search_cancel_btn_1.setGeometry(QtCore.QRect(150, 80, 21, 31))
        self.search_cancel_btn_1.setStyleSheet("\n"
                                               "font: 75 10pt \"MS Shell Dlg 2\";")
        self.search_cancel_btn_1.setObjectName("search_cancel_btn_1")
        self.search_cancel_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.search_cancel_btn_2.setGeometry(QtCore.QRect(370, 80, 21, 31))
        self.search_cancel_btn_2.setStyleSheet("\n"
                                               "font: 75 10pt \"MS Shell Dlg 2\";")
        self.search_cancel_btn_2.setObjectName("search_cancel_btn_2")
        #search box ends

        # Pagination
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(210, 380, 231, 41))
        self.widget.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.widget.setObjectName("widget")
        self.btn_1 = QtWidgets.QPushButton(self.widget)
        self.btn_1.setGeometry(QtCore.QRect(70, 10, 31, 23))
        self.btn_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.left_btn = QtWidgets.QPushButton(self.widget)
        self.left_btn.setGeometry(QtCore.QRect(40, 10, 31, 23))
        self.left_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.left_btn.setObjectName("left_btn")
        self.btn_2 = QtWidgets.QPushButton(self.widget)
        self.btn_2.setGeometry(QtCore.QRect(100, 10, 31, 23))
        self.btn_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.widget)
        self.btn_3.setGeometry(QtCore.QRect(130, 10, 31, 23))
        self.btn_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.right_btn = QtWidgets.QPushButton(self.widget)
        self.right_btn.setGeometry(QtCore.QRect(160, 10, 31, 23))
        self.right_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.right_btn.setObjectName("right_btn")
        self.last_btn = QtWidgets.QPushButton(self.widget)
        self.last_btn.setGeometry(QtCore.QRect(190, 10, 31, 23))
        self.last_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.last_btn.setObjectName("last_btn")
        self.first_btn = QtWidgets.QPushButton(self.widget)
        self.first_btn.setGeometry(QtCore.QRect(10, 10, 35, 23))
        self.first_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.first_btn.setObjectName("first_btn")
        # Pagination over

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.display(client)
        # button click events
        self.objs[0][3].clicked.connect(lambda : self.openPDFViewer(self.objs[0][5]))
        self.objs[1][3].clicked.connect(lambda : self.openPDFViewer(self.objs[1][5]))
        self.objs[2][3].clicked.connect(lambda : self.openPDFViewer(self.objs[2][5]))
        self.objs[3][3].clicked.connect(lambda : self.openPDFViewer(self.objs[3][5]))
        self.objs[4][3].clicked.connect(lambda : self.openPDFViewer(self.objs[4][5]))
        self.objs[4][3].clicked.connect(lambda : self.openPDFViewer(self.objs[4][5]))

        # self.labelfile_btn.clicked.connect(self.openLabelWindow)
        self.btn_1.clicked.connect(self.changeCurPage1)
        self.btn_2.clicked.connect(self.changeCurPage2)
        self.btn_3.clicked.connect(self.changeCurPage3)

        self.right_btn.clicked.connect(self.RBtn)
        self.left_btn.clicked.connect(self.LBtn)

        self.first_btn.clicked.connect(self.firstBtn)
        self.last_btn.clicked.connect(self.lastBtn)

        self.search_btn_1.clicked.connect(self.searchByName)
        self.search_btn_2.clicked.connect(self.searchByCategory)
        self.search_cancel_btn_1.clicked.connect(self.cancelSearchByName)
        self.search_cancel_btn_2.clicked.connect(self.cancelSearchByCategory)
        # button click events over

    # open PDF viewer
    def openPDFViewer(self, _id):
        print(_id)
        originalPath=self.all_data[_id-1]["Path"]

        # originalPath= "C:/Users/BAVISKAR/Desktop/BE_Project/Github/Be_Project/20_newsgroups/alt.atheism/51139"
        # print(originalPath)
        # print(type(originalPath))

        file_path = originalPath+".txt"     # clone of file with .txt extension
        shutil.copyfile(originalPath, file_path)    # copy the content into clone file

        # operations on clone file
        file_name=os.path.split(file_path) # split filepath at /
        file_name=os.path.splitext(file_name[1])    # split the filename at extension
        file_name=file_name[0]  # just take the filename

        PdfViewer(file_path, file_name) # call pdf viewer
        if os.path.exists(file_path):
            os.remove(file_path)    # delete dummy file

    # open label file window
    def openLabelWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LabelFileWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # show data from database for current page no
    def pagination(self):
        self.page_no=self.cur_page_no
        self.cur_page_no-=1
        self.total_pages= int(self.data_len/5) if self.data_len%5==0 else int((self.data_len/5)+1)

        self.cur_start_page=(5*self.cur_page_no)
        self.cur_end_page=self.cur_start_page+5

        self.reqData = self.all_data[self.cur_start_page:self.cur_end_page]
        self.printData()

    # print data on screen
    def printData(self):

        if (int(self.btn_1.text())==self.page_no):
            self.btn_1.setStyleSheet("background-color: rgb(170, 255, 255);")
            self.btn_2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.btn_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        elif (int(self.btn_2.text())==self.page_no):
            self.btn_2.setStyleSheet("background-color: rgb(170, 255, 255);")
            self.btn_1.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.btn_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        elif (int(self.btn_3.text())==self.page_no):
            self.btn_3.setStyleSheet("background-color: rgb(170, 255, 255);")
            self.btn_1.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.btn_2.setStyleSheet("background-color: rgb(255, 255, 255);")

        if self.flag==0:
            self.objs = []
            self.y_line = 110
            self.y_label = 140
            self.y_status = 140
            self.y_view = 130
            self.y_label_file = 130
            i = 1
            d = 0
            for data in self.reqData:
                temp=[]

                self.startline = QtWidgets.QFrame(self.centralwidget)
                self.startline.setGeometry(QtCore.QRect(30, self.y_line, 411, 21))
                self.startline.setFrameShape(QtWidgets.QFrame.HLine)
                # self.startline.setObjectName("startline_" + str(i))
                self.startline.setFrameShadow(QtWidgets.QFrame.Sunken)
                temp.append(self.startline)


                self.filename_label = QtWidgets.QLabel(self.centralwidget)
                self.filename_label.setGeometry(30, self.y_label, 141, 16)
                self.filename_label.setText(data['Name'])
                # self.filename_label.setObjectName("filename_label_"+str(i))
                print(data['Name'])
                temp.append(self.filename_label)

                self.file_label = QtWidgets.QLabel(self.centralwidget)
                self.file_label.setGeometry(126, self.y_status, 121, 20)
                self.file_label.setAlignment(QtCore.Qt.AlignRight)
                if data["Status"] == "Labeled":
                    self.file_label.setText(data['Category'])
                else:
                    self.file_label.setText("Unlabeled")
                # self.file_label.setObjectName("filename_label_" + str(i))
                temp.append(self.file_label)

                self.view_btn = QtWidgets.QPushButton(self.centralwidget)
                self.view_btn.setGeometry(QtCore.QRect(270, self.y_view, 81, 31))
                self.view_btn.setText("View")
                # self.view_btn.setObjectName("view_btn_" + str(i))
                temp.append(self.view_btn)

                self.labelfile_btn = QtWidgets.QPushButton(self.centralwidget)
                self.labelfile_btn.setGeometry(QtCore.QRect(360, self.y_label_file, 81, 31))
                self.labelfile_btn.setText("Label File")
                # self.labelfile_btn.setObjectName("labelfile_btn_" + str(i))
                temp.append(self.labelfile_btn)

                temp.append(data["_id"])

                self.objs.append(temp)

                self.y_line += 50
                self.y_label += 50
                self.y_status += 50
                self.y_view += 50
                self.y_label_file += 50
                d += 50
                i += 1
                self.flag=1
        else:
            cnt=5
            for data, x in zip(self.reqData, self.objs):
                cnt-=1
                x[1].setText(data['Name'])
                x[2].setText(data['Category'])
                x[0].show()
                x[1].show()
                x[2].show()
                x[3].show()
                x[4].show()

                x[5]=data['_id']
            if cnt:
                self.tempObj=self.objs[-cnt:]
                for c, x in zip(range(cnt), self.tempObj):
                    cnt-=1
                    x[0].hide()
                    x[1].hide()
                    x[2].hide()
                    x[3].hide()
                    x[4].hide()

        self.cur_page_no+=1

    # change cur page no to the button number clicked
    def changeCurPage1(self):
        self.cur_page_no=int(self.btn_1.text())
        self.cursor=1
        print(self.cur_page_no)
        self.pagination()
    # change cur page no to the button number clicked
    def changeCurPage2(self):
        self.cur_page_no=int(self.btn_2.text())
        self.cursor = 2
        self.pagination()
    # change cur page no to the button number clicked
    def changeCurPage3(self):
        self.cur_page_no=int(self.btn_3.text())
        self.cursor = 3
        self.pagination()

    # right arrow button event
    def RBtn(self):

            if self.cursor==3 and self.cur_page_no!=self.total_pages:
                if (int(self.btn_1.text()) + 1 <= self.total_pages):
                    self.btn_1.setText(str(int(self.btn_1.text()) + 1))
                if (int(self.btn_2.text()) + 1 <= self.total_pages):
                    self.btn_2.setText(str(int(self.btn_2.text()) + 1))
                else:
                    self.btn_2.hide()
                    self.hidden[1] = True
                if (int(self.btn_3.text()) + 1 <= self.total_pages):
                    self.btn_3.setText(str(int(self.btn_3.text()) + 1))
                else:
                    self.btn_3.hide()
                    self.hidden[2] = True

            self.cursor = self.cursor+1 if self.cursor+1<=3 else self.cursor
            self.cur_page_no= self.cur_page_no+1 if self.cur_page_no + 1 <= self.total_pages else self.cur_page_no
            self.pagination()
    # left arrow button event
    def LBtn(self):

            if self.cur_page_no==self.total_pages and self.cursor<3:
                if self.cursor==1:
                    if (int(self.btn_1.text()) - 1 >= 1):
                        self.btn_1.setText(str(self.total_pages - 1))
                    self.btn_2.show()
                    self.hidden[1] = False
                    self.btn_2.setText(str(self.total_pages))

                elif self.cursor==2:
                    if (int(self.btn_1.text()) - 1 >= 1):
                        self.btn_1.setText(str(int(self.btn_1.text()) - 1))
                    if (int(self.btn_2.text()) - 1 >= 1):
                        self.btn_2.setText(str(int(self.btn_2.text()) - 1))
                    self.btn_3.show()
                    self.hidden[2] = False
                    self.btn_3.setText(str(self.total_pages))
                    self.cursor=3
                self.cur_page_no -= 1
                self.pagination()
                return

            elif self.cursor == 1 and int(self.btn_1.text())!=1:
                if (int(self.btn_1.text()) - 1 >=1):
                    self.btn_1.setText(str(int(self.btn_1.text()) - 1))
                if (int(self.btn_2.text()) - 1 >=1):
                    self.btn_2.setText(str(int(self.btn_2.text()) - 1))
                # else:
                #     self.btn_2.hide()
                if (int(self.btn_3.text()) - 1 >=1):
                    if self.hidden[2]:
                        self.btn_3.show()
                        self.hidden[2]=False
                        self.btn_3.setText(str(self.total_pages))
                    else:
                        self.btn_3.setText(str(int(self.btn_3.text()) - 1))
                # else:
                #     self.btn_3.hide()

            self.cursor = self.cursor - 1 if self.cursor - 1 >= 1 else self.cursor
            self.cur_page_no = self.cur_page_no - 1 if self.cur_page_no - 1 >= 1 else self.cur_page_no
            self.pagination()
    # first button event
    def firstBtn(self):
        self.cursor=1
        self.cur_page_no=1

        self.btn_1.setText("1")
        if self.total_pages>=2:
            if self.hidden[1]:
                self.btn_2.show()
                self.hidden[1] = False
            self.btn_2.setText("2")
        else:
            self.btn_2.hide()
            self.hidden[1] = True
        if self.total_pages>=3:
            if self.hidden[2]:
                self.btn_3.show()
                self.hidden[2] = False
            self.btn_3.setText("3")
        else:
            self.btn_3.hide()
            self.hidden[2] = True

        self.pagination()
    # last button event
    def lastBtn(self):
        self.cur_page_no=self.total_pages

        if self.cur_page_no%3==1:
            self.btn_1.setText(str(self.cur_page_no))
            self.btn_2.hide()
            self.hidden[1]=True
            self.btn_3.hide()
            self.hidden[2] = True
            self.cursor=1
        elif self.cur_page_no%3==2:
            self.btn_1.setText(str(self.cur_page_no-1))
            self.btn_2.setText(str(self.cur_page_no))
            self.btn_3.hide()
            self.hidden[2] = True
            self.cursor=2
        elif self.cur_page_no%3==0:
            self.btn_1.setText(str(self.cur_page_no - 2))
            self.btn_2.setText(str(self.cur_page_no-1))
            self.btn_3.setText(str(self.cur_page_no))
            self.cursor=3

        self.pagination()

    # dynamic display of data from database
    def display(self, client):
        print("in display")
        db = client['AutoReview']  # database object
        self.collection_name = db['AllDocuments']  # collection object

        info_collection_name = db['OrgInfo']
        name=info_collection_name.find_one({})
        self.title_label.setText(name["Title"])

        self.all_data = list(self.collection_name.find({}))
        self.data_len = self.collection_name.count_documents({})
        print(self.data_len)
        self.flag=0
        self.hidden = [False, False, False]
        self.cur_page_no = 1
        self.cursor=1
        self.searchBy = [0, 0]
        self.btn_1.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pagination()

    # search records by name
    def searchByName(self):
        self.searchBy[0]=1
        self.searchName=self.search_txt_1.toPlainText()
        if self.searchBy[1]:
            self.all_data = list(self.collection_name.find({"Name": self.searchName, "Category":self.searchCategory}))
            self.data_len = self.collection_name.count_documents({"Name": self.searchName, "Category":self.searchCategory})
        else:
            self.all_data = list(self.collection_name.find({"Name":self.searchName}))
            self.data_len = self.collection_name.count_documents({"Name":self.searchName})
        self.cur_page_no = 1

        self.total_pages = int(self.data_len / 5) if self.data_len % 5 == 0 else int((self.data_len / 5) + 1)

        self.page_no = self.cur_page_no
        self.cur_page_no -= 1
        self.cur_start_page = (5 * self.cur_page_no)
        self.cur_end_page = self.cur_start_page + 5

        self.reqData = self.all_data[self.cur_start_page:self.cur_end_page]

        self.printData()
    # clear search records by name
    def cancelSearchByName(self):
        self.searchBy[0]=0
        self.search_txt_1.setPlainText("")
        if self.searchBy[1]:
            self.all_data = list(self.collection_name.find({"Category":self.searchCategory}))
            self.data_len = self.collection_name.count_documents({"Category":self.searchCategory})
        else:
            self.all_data = list(self.collection_name.find({}))
            self.data_len = self.collection_name.count_documents({})
        self.cur_page_no = 1

        self.total_pages = int(self.data_len / 5) if self.data_len % 5 == 0 else int((self.data_len / 5) + 1)

        self.page_no = self.cur_page_no
        self.cur_page_no -= 1
        self.cur_start_page = (5 * self.cur_page_no)
        self.cur_end_page = self.cur_start_page + 5

        self.reqData = self.all_data[self.cur_start_page:self.cur_end_page]

        self.printData()

    # search records by category
    def searchByCategory(self):
        self.searchBy[1] = 1
        self.searchCategory = self.search_txt_2.toPlainText()
        if self.searchBy[0]:
            self.all_data = list(self.collection_name.find({"Name": self.searchName, "Category": self.searchCategory}))
            self.data_len = self.collection_name.count_documents(
                {"Name": self.searchName, "Category": self.searchCategory})
        else:
            self.all_data = list(self.collection_name.find({"Category": self.searchCategory}))
            self.data_len = self.collection_name.count_documents({"Category": self.searchCategory})
        self.cur_page_no = 1

        self.total_pages = int(self.data_len / 5) if self.data_len % 5 == 0 else int((self.data_len / 5) + 1)

        self.page_no = self.cur_page_no
        self.cur_page_no -= 1
        self.cur_start_page = (5 * self.cur_page_no)
        self.cur_end_page = self.cur_start_page + 5

        self.reqData = self.all_data[self.cur_start_page:self.cur_end_page]

        self.printData()
    # clear search records by catgory
    def cancelSearchByCategory(self):
        self.searchBy[1]=0
        self.search_txt_2.setPlainText("")
        if self.searchBy[0]:
            self.all_data = list(self.collection_name.find({"Name": self.searchName}))
            self.data_len = self.collection_name.count_documents({"Name": self.searchName})
        else:
            self.all_data = list(self.collection_name.find({}))
            self.data_len = self.collection_name.count_documents({})
        self.cur_page_no = 1

        self.total_pages = int(self.data_len / 5) if self.data_len % 5 == 0 else int((self.data_len / 5) + 1)

        self.page_no = self.cur_page_no
        self.cur_page_no -= 1
        self.cur_start_page = (5 * self.cur_page_no)
        self.cur_end_page = self.cur_start_page + 5

        self.reqData = self.all_data[self.cur_start_page:self.cur_end_page]

        self.printData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Title"))
        # self.view_btn.setText(_translate("MainWindow", "View "))
        # self.filename_label.setText(_translate("MainWindow", "File 1*"))
        # self.groups_10.setText(_translate("MainWindow", "View "))
        # self.label_4.setText(_translate("MainWindow", "File 2"))
        # self.groups_11.setText(_translate("MainWindow", "View "))
        # self.label_5.setText(_translate("MainWindow", "File 3"))
        # self.groups_12.setText(_translate("MainWindow", "View "))
        # self.label_6.setText(_translate("MainWindow", "File 4"))
        # self.labelfile_btn.setText(_translate("MainWindow", "Label file"))
        # self.groups_13.setText(_translate("MainWindow", "Label file"))
        # self.groups_14.setText(_translate("MainWindow", "Label file"))
        # self.groups_15.setText(_translate("MainWindow", "Label file"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.left_btn.setText(_translate("MainWindow", "<"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.right_btn.setText(_translate("MainWindow", ">"))
        self.last_btn.setText(_translate("MainWindow", "LAST"))
        self.first_btn.setText(_translate("MainWindow", "FIRST"))
        self.submit_btn.setText(_translate("MainWindow", "Submit"))
        self.search_btn_1.setText(_translate("MainWindow", "search"))
        self.search_btn_2.setText(_translate("MainWindow", "search"))
        self.search_cancel_btn_1.setText(_translate("MainWindow", "X"))
        self.search_cancel_btn_2.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RealDatasetWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


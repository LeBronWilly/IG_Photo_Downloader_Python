# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IG_Photo_Downloader_UI_V01YHMFKj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_IG_Photo_Downloader(object):
    def setupUi(self, IG_Photo_Downloader):
        if not IG_Photo_Downloader.objectName():
            IG_Photo_Downloader.setObjectName(u"IG_Photo_Downloader")
        IG_Photo_Downloader.resize(967, 544)
        self.Username_Text = QTextEdit(IG_Photo_Downloader)
        self.Username_Text.setObjectName(u"Username_Text")
        self.Username_Text.setGeometry(QRect(230, 230, 465, 51))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Username_Text.setFont(font)
        self.Username_Text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Username_Text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_1 = QLabel(IG_Photo_Downloader)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(30, 240, 200, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_1.setFont(font1)
        self.label_1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_7 = QLabel(IG_Photo_Downloader)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 370, 200, 31))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Date_ComboBox = QComboBox(IG_Photo_Downloader)
        self.Date_ComboBox.addItem("")
        self.Date_ComboBox.setObjectName(u"Date_ComboBox")
        self.Date_ComboBox.setGeometry(QRect(230, 360, 465, 51))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(16)
        self.Date_ComboBox.setFont(font2)
        self.Search_Button = QPushButton(IG_Photo_Downloader)
        self.Search_Button.setObjectName(u"Search_Button")
        self.Search_Button.setEnabled(True)
        self.Search_Button.setGeometry(QRect(740, 240, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.Search_Button.setFont(font3)
        self.Download_Button = QPushButton(IG_Photo_Downloader)
        self.Download_Button.setObjectName(u"Download_Button")
        self.Download_Button.setEnabled(False)
        self.Download_Button.setGeometry(QRect(740, 370, 181, 31))
        self.Download_Button.setFont(font3)
        self.Refresh_Button = QPushButton(IG_Photo_Downloader)
        self.Refresh_Button.setObjectName(u"Refresh_Button")
        self.Refresh_Button.setEnabled(True)
        self.Refresh_Button.setGeometry(QRect(740, 470, 181, 41))
        self.Refresh_Button.setFont(font3)
        self.Account_Text = QTextEdit(IG_Photo_Downloader)
        self.Account_Text.setObjectName(u"Account_Text")
        self.Account_Text.setGeometry(QRect(30, 110, 431, 41))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(16)
        font4.setBold(False)
        font4.setWeight(50)
        self.Account_Text.setFont(font4)
        self.Account_Text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Account_Text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_2 = QLabel(IG_Photo_Downloader)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 301, 31))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_3 = QLabel(IG_Photo_Downloader)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 70, 301, 31))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Password_Text = QLineEdit(IG_Photo_Downloader)
        self.Password_Text.setObjectName(u"Password_Text")
        self.Password_Text.setGeometry(QRect(490, 110, 431, 41))
        self.Password_Text.setFont(font2)
        self.Password_Text.setEchoMode(QLineEdit.Password)
        self.label_6 = QLabel(IG_Photo_Downloader)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 500, 411, 31))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(True)
        font5.setWeight(75)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4 = QLabel(IG_Photo_Downloader)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 160, 471, 31))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_4.setFont(font6)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_1.raise_()
        self.label_7.raise_()
        self.Username_Text.raise_()
        self.Date_ComboBox.raise_()
        self.Search_Button.raise_()
        self.Download_Button.raise_()
        self.Refresh_Button.raise_()
        self.Account_Text.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.Password_Text.raise_()
        self.label_6.raise_()
        self.label_4.raise_()

        self.retranslateUi(IG_Photo_Downloader)

        QMetaObject.connectSlotsByName(IG_Photo_Downloader)
    # setupUi

    def retranslateUi(self, IG_Photo_Downloader):
        IG_Photo_Downloader.setWindowTitle(QCoreApplication.translate("IG_Photo_Downloader", u"IG_Photo_Downloader", None))
        self.Username_Text.setHtml(QCoreApplication.translate("IG_Photo_Downloader", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">kobebryant</p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("IG_Photo_Downloader", u"IG Username: ", None))
        self.label_7.setText(QCoreApplication.translate("IG_Photo_Downloader", u"Post Dates: ", None))
        self.Date_ComboBox.setItemText(0, QCoreApplication.translate("IG_Photo_Downloader", u"Choose Date to Download", None))

        self.Date_ComboBox.setCurrentText(QCoreApplication.translate("IG_Photo_Downloader", u"Choose Date to Download", None))
        self.Search_Button.setText(QCoreApplication.translate("IG_Photo_Downloader", u"Search", None))
        self.Download_Button.setText(QCoreApplication.translate("IG_Photo_Downloader", u"Download", None))
        self.Refresh_Button.setText(QCoreApplication.translate("IG_Photo_Downloader", u"Refresh All", None))
        self.Account_Text.setHtml(QCoreApplication.translate("IG_Photo_Downloader", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'PMingLiU';\">xxx@gmail.com</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("IG_Photo_Downloader", u"Your IG Account: ", None))
        self.label_3.setText(QCoreApplication.translate("IG_Photo_Downloader", u"Your IG Password: ", None))
        self.label_6.setText(QCoreApplication.translate("IG_Photo_Downloader", u"Developed by Willy Fang", None))
        self.label_4.setText(QCoreApplication.translate("IG_Photo_Downloader", u"You have to login to download IG photos", None))
    # retranslateUi


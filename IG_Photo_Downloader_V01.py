# -*- coding: utf-8 -*-
"""
Created on 08/28, 2020
@author: Willy Fang

"""
# https://shengyu7697.github.io/python-pyqt-qmessagebox/
# https://pythonprogramminglanguage.com/pyqt5-message-box/
# https://steam.oxxostudio.tw/category/python/basic/try-except.html


from UI_V01 import *
import instaloader
import os
import glob
from PySide2.QtWidgets import QMessageBox

ig = instaloader.Instaloader()


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_IG_Photo_Downloader()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()

    def setup_control(self):
        # profile = instaloader.Profile.from_username(ig.context, ig_username)
        # posts = list(profile.get_posts())
        # dates_list = [post.date.strftime("%Y/%m/%d %H:%M:%S") for post in posts]

        self.ui.Search_Button.clicked.connect(
            lambda: self.Search_Button_Clicked(self.ui.Account_Text.toPlainText(),
                                               self.ui.Password_Text.text(),
                                               self.ui.Username_Text.toPlainText()))
        self.ui.Date_ComboBox.currentTextChanged.connect(self.Date_ComboBox_Select_Change)
        self.ui.Refresh_Button.clicked.connect(self.Refresh_Button_Clicked)

    def Search_Button_Clicked(self, account, password, username):
        if account == "" or password == "":
            QMessageBox.information(self, "Error", "Please enter your IG account/password")
        elif username == "":
            QMessageBox.information(self, "Error", "Please enter the target's IG username")
        else:
            try:
                ig.login(account, password)
            except Exception:
                QMessageBox.information(self, "Error", "Wrong IG account/password")
            else:
                try:
                    profile = instaloader.Profile.from_username(ig.context, username)
                except Exception:
                    QMessageBox.information(self, "Error", "IG username \"" + username + "\" does not exist")
                else:
                    self.ui.Date_ComboBox.clear()
                    self.ui.Date_ComboBox.addItem("Choose Date to Download")
                    self.ui.posts = list(profile.get_posts())
                    self.ui.dates_list = [str(ind + 1) + ". " + post.date.strftime("%Y/%m/%d %H:%M:%S")
                                          for ind, post in enumerate(self.ui.posts)]
                    for date in self.ui.dates_list:
                        self.ui.Date_ComboBox.addItem(date)
                    QMessageBox.information(self, "Success", "Login Success\nSearch Success\n       ^o^")
                    self.ui.Download_Button.clicked.connect(
                        lambda: self.Download_Button_Clicked(self.ui.posts, self.ui.dates_list, username))

    def Download_Button_Clicked(self, posts, dates_list, username):
        ig.download_post(posts[dates_list.index(self.ui.Date_ComboBox.currentText())], username)
        delete_list = glob.glob(username + '/*.json.xz')
        for d in delete_list:
            os.remove(d)

    def Date_ComboBox_Select_Change(self):
        if self.ui.Date_ComboBox.currentText() != "Choose Date to Download":
            self.ui.Download_Button.setEnabled(True)
        else:
            self.ui.Download_Button.setEnabled(False)

    def Refresh_Button_Clicked(self):
        self.ui.Date_ComboBox.clear()
        self.ui.Date_ComboBox.addItem("Choose Date to Download")
        self.ui.Account_Text.setText("xxx@gmail.com")
        self.ui.Password_Text.setText("")
        self.ui.Username_Text.setText("kobebryant")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    IG_Photo_Downloader = AppWindow()
    IG_Photo_Downloader.show()
    sys.exit(app.exec_())


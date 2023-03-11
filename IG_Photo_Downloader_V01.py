# -*- coding: utf-8 -*-
"""
Created on 08/28, 2022
@author: Willy Fang

"""
# https://instaloader.github.io/index.html
# https://stackoverflow.com/questions/71182479/download-only-instagram-videos-with-instaloader
# https://instaloader.github.io/module/structures.html#posts
# https://stackoverflow.com/questions/71182479/download-only-instagram-videos-with-instaloader
# https://samjason515.medium.com/超簡單instagram-爬蟲套件-instaloader-ad3ec7016fa2
# https://shengyu7697.github.io/python-pyqt-qmessagebox/
# https://pythonprogramminglanguage.com/pyqt5-message-box/
# https://steam.oxxostudio.tw/category/python/basic/try-except.html
# https://stackoverflow.com/questions/11625062/cant-remove-a-folder-with-os-remove-windowserror-error-5-access-is-denied
# https://stackoverflow.com/questions/45134102/shutil-move-if-directory-already-exists
# https://docs.python.org/3/library/shutil.html
# https://linuxhint.com/overwrite-file-python/
# https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/
# https://datatofish.com/move-file-python/


from UI_V01 import *
import instaloader
import os
import glob
from PySide2.QtWidgets import QMessageBox
import shutil
import urllib.request

ig = instaloader.Instaloader()


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_IG_Photo_Downloader()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()

    def setup_control(self):
        self.ui.IG_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/IG_Photo_Downloader_Python/main/IG_icon.png'
        img_data = urllib.request.urlopen(url).read()
        self.ui.IG_img.loadFromData(img_data)
        self.ui.IG_img = self.ui.IG_img.scaled(75, 75)
        self.setWindowIcon(QIcon(self.ui.IG_img))

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
        ig.download_post(post=posts[dates_list.index(self.ui.Date_ComboBox.currentText())],
                         target=username)
        delete_list = glob.glob(username + '/*.json.xz')
        for d in delete_list:
            os.remove(d)
        if not os.path.exists("Downloaded Photo/"+username):
            shutil.move(username, "Downloaded Photo/"+username)
        else:
            for file_path in glob.glob(username + '/*'):
                shutil.copy2(file_path, "Downloaded Photo/" + username)
            shutil.rmtree(username)
        QMessageBox.information(self, "Success", "Download Success ^o^")

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


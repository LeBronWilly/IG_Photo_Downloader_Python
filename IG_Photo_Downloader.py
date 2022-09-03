# -*- coding: utf-8 -*-
"""
Created on 08/28, 2020
@author: Willy Fang

"""
from UI_V01 import *
import instaloader
import os
import glob

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_IG_Photo_Downloader()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()


    def setup_control(self):
        ig = instaloader.Instaloader()

        ig_username = "patbev21"

        profile = instaloader.Profile.from_username(ig.context, ig_username)
        posts = list(profile.get_posts())
        dates_list = [post.date.strftime("%Y/%m/%d %H:%M:%S") for post in posts]

    def Search_Button_Clicked(self):

        pass



    def Download_Button_Clicked(self):

        pass











if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    IG_Photo_Downloader = AppWindow()
    IG_Photo_Downloader.show()
    sys.exit(app.exec_())


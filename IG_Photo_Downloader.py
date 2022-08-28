# -*- coding: utf-8 -*-
"""
Created on 08/28, 2020
@author: Willy Fang

"""

import requests
from bs4 import BeautifulSoup


my_headers = {'cookie': 'over18=1;'}
IG_html = requests.get("https://www.instagram.com/p/ChnyHzGNFtC/", my_headers)
print(IG_html.status_code)

IG_bs4 = BeautifulSoup(IG_html.text, 'html.parser')
# print(IG_bs4.prettify())
print(IG_bs4.find_all("img")[0])
# print(len(IG_bs4.find_all("img")))






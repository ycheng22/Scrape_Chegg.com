# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:53:33 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url_beg = "https://www.chegg.com/homework-help/questions-and-answers/physics-archive-"
url_date = "2021-april-03?"
url_page = "page=30"
url = url_beg + url_date + url_page

domain=Request(url)
domain.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')
response =urlopen(domain)
bs = BeautifulSoup(response, 'html.parser')

mydivs = bs.find_all("div", {"class": "txt-body question-body"})

question = []
link = []
for idx in range(len(mydivs)):
    q_text = mydivs[idx].get_text().replace('\n', '')
    lk = mydivs[idx].a['href']
    question.append(q_text)
    link.append(lk)
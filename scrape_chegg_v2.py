# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:06:09 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
https://www.chegg.com/homework-help/questions-and-answers/physics-archive-2021-april

"""
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time
tic = time.time()
import sys
import warnings
warnings.filterwarnings("ignore")
    
url_beg = "https://www.chegg.com/homework-help/questions-and-answers/physics-archive-"
url_date = "2021-april-04?"
out_filename = 'question_April_4.csv'
max_page = 52 #check from the page, data: page_num, total_questions
#april2:46, 4542; april3: 36, 3584; april4：52, 5128; april5:
################################################################   
question = [] 
link = []
for pg_num in range(1, max_page+1):
    sys.stdout.write("\r scrapping %d / %d" %(pg_num, max_page))
    sys.stdout.flush()
    url_page = "page=" + str(pg_num)
    url = url_beg + url_date + url_page
    domain=Request(url)
    domain.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')
    response =urlopen(domain)
    #bs = BeautifulSoup(response, 'html.parser')
    bs = BeautifulSoup(response, 'html.parser', from_encoding="iso-8859-1")
    mydivs = bs.find_all("div", {"class": "txt-body question-body"})
    
    for idx in range(len(mydivs)):
        q_text = mydivs[idx].get_text().replace('\n', '')
        lk = mydivs[idx].a['href']
        lk = "https://www.chegg.com/" + lk
        question.append(q_text)
        link.append(lk)
    time.sleep(2)

df_question_link = pd.DataFrame({'link': link, 'question': question})
df_question_link.to_csv(out_filename, encoding = "utf-8")
toc = time.time()
print("\n Time elapsed:", toc - tic, "seconds")  
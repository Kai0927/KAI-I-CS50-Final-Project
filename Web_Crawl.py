from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.chrome.service import Service

import os
from cs50 import SQL

db = SQL("sqlite:///Atmosphere_glossary.db")

link = "http://www.wrds.uwyo.edu/sco/climateatlas/glossary.html?fbclid=IwAR2XSTgiBEadC1Rnn0yqIJ2vvMDGjNZ5p36ZL3FlR2LlUVTHksE8icN5dsQ"

service = Service(executable_path='/home/kai0927/bin/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(service=service, options=options)

chrome.get(link)

time.sleep(5.0 + random.random())

soup = BeautifulSoup(chrome.page_source, 'html.parser')
temp = soup.get_text()

articles = soup.find_all("p")

out = []; out1=[]
for article in articles:
    if (str(article.select_one('b'))!='None'):
        out.append('What is '+ article.select_one('b').getText()+'?')
        out1.append(str(article))

### clean data and put it into sqlite ###    
out3 = []
for i in range(len(out1)):
    clean_a = str(out1[i]).replace("</p>", "").replace("<p><b>", "").replace('</b></p>', "").replace("<b>", "").replace("\n", " ").replace("</b>", ":")
    out3.append(clean_a)

    db.execute("INSERT INTO Q_A (question, answer) VALUES (?, ?)",
                out[i], out3[i])


q = out   
a = out3

print(len(q),' ', len(a))    

qustion =  q 
answer = a 

print(len(qustion),' ',len(answer))
print('end')

# coding: utf-8

# In[ ]:


# Scraping stock prices for companies on Dow Jones Average


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas 
import re
date = "10-11-2017"


# In[3]:


# Extracting data from the first page only
base_url = "http://money.cnn.com/data/markets/dow/?page="
l = []


# In[4]:


for i in range(0,2):
    r = requests.get(base_url + str(i+1))
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    
    # print(soup.prettify())
    all = soup.find_all("div", {"class": "wsod_dataTableBorder"})
    list1 = all[1].find_all("a", {"class": "wsod_symbol"})
    list2 = all[1].find_all("span",{"stream":re.compile('last_*')})
    list3 = all[1].find_all("span",{"stream":re.compile('change*')})
    list4 = all[1].find_all("span",{"stream":re.compile('changePct_*')})
    list5 = all[1].find_all("td")

    for i in range(len(list1)):
        d={}
        d['1.Company'] = list1[i].text
        d['2.Price'] = list2[i].text
        d['3.Change'] = list3[2*i].text   
        d['4.PctChange'] = list4[i].text
        d['5.P/E'] = list5[4+7*i].text
        d['6.Vol'] = list5[5+7*i].text
        l.append(d)


# In[5]:


df = pandas.DataFrame(l)
df.to_csv("DowJones_"+date+"_1.csv")


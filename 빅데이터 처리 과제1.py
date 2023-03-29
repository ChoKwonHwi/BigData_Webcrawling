#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


result = []
sido2page = [0, 26, 17, 9, 11, 6, 6, 6, 17, 45, 19, 16, 18, 16, 23, 25, 23, 3]


# In[3]:


for sido1 in range(1, 18) :
    pagenum = sido2page[sido1]
    for sido2 in range(1, pagenum):
        kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1={0}&sido2={1}&txtsearch='.format(sido1, sido2)
        html = urllib.request.urlopen(kyochon_url)
        soupkyochon = BeautifulSoup(html, 'html.parser')
        tag_ul = soupkyochon.find('ul', 'list')
        for store in tag_ul.find_all('li') :
            if len(store) <= 3 :
                break
            store_name = store.find('strong').string
            store_em = store.select_one('em').get_text().split()
            store_sido = store_em[0]
            store_gungu = store_em[1]
            store_address = store_em[0] + " " + store_em[1] + " " + store_em[2] + " " + store_em[3]
            result.append([store_name]+[store_sido]+[store_gungu]+[store_address])


# In[4]:


len(result)


# In[5]:


result


# In[6]:


kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido', 'gungu', 'address'))


# In[7]:


kyochon_tbl.to_csv("./kyochon.csv", encoding = "cp949", mode = "w", index = True)


# In[8]:


kyochon_data = pd.read_csv("./kyochon.csv", encoding = "cp949")
kyochon_data.tail(5)


# In[ ]:





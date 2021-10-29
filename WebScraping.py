#!/usr/bin/env python
# coding: utf-8

# ##########Below code scrapes the names of the books against each book for all the webpages.

# In[55]:


import requests
import bs4
two_star_titles = []
for i in range(1,51):
    URL = "https://books.toscrape.com/catalogue/page-{}.html".format(i)
    re=requests.get(URL)
    soup=bs4.BeautifulSoup(re.text,'lxml')
    products=soup.select(".product_pod")
    for book in products:
        if len(book.select(".star-rating.Three"))!=0:
            book_title=book.select("a")[1]["title"]
            two_star_titles.append(book_title)
print(two_star_titles)
    
    


# #######Below code scrapes the author details from the website.

# In[3]:


import requests
import bs4
authors=set()
for i in range(0,11):
    base_url="https://quotes.toscrape.com/page/{}/".format(i)
    re= requests.get(base_url)
    soup=bs4.BeautifulSoup(re.text,'lxml')
    #quot=soup.select(".quote")
    auth=soup.select(".author")
    for authorr in auth:
        authors.add(authorr.text)
print(authors)


# ######Below code scrapes the quotes in every page from the website.

# In[4]:


import requests
import bs4
quotes=[]
for i in range(1,11):
    base_url="https://quotes.toscrape.com/page/{}/".format(i)
    re= requests.get(base_url)
    soup=bs4.BeautifulSoup(re.text,'lxml')
    #quot=soup.select(".quote")
    auth=soup.select(".text")
    for authorr in auth:
        quotes.append(authorr.text)
print(quotes)


# #######Below code scrapes the tagged item on the website

# In[28]:


import requests
import bs4
tags=[]
base_url="https://quotes.toscrape.com/page/1/"
re= requests.get(base_url)
soup=bs4.BeautifulSoup(re.text,'lxml')
#quot=soup.select(".quote")
auth=soup.select(".tag-item")
for tag in auth:
    tags.append(tag.text)
print([i.strip('\n') for i in tags]) 


# ########Below code scrapes the average temperature andaverage humidity for the period of 01/01/2009 to 08/05/2020 and converts the data to a dataframe and loads it into a pickle file.

# In[47]:


import requests
import bs4
base_url="http://www.estesparkweather.net/archive_reports.php?date=210621"
re= requests.get(base_url)
soup=bs4.BeautifulSoup(re.text,'lxml')
table=soup.find_all('table')[0]
temp=table.find_all('tr',class_='column-light')[0].text
hum=table.find_all('tr',class_='column-dark')[0].text
print(temp)
print(hum)
    


# In[154]:


import requests
import bs4
from datetime import timedelta, date, datetime


today = datetime.now()
num_days=7
list_format =[today + timedelta(days=i) for i in range(num_days)]
actual =[date.strftime("%d%m%y") for date in list_format]
#print(actual)
temp_new=[]
hum_new=[]
for data in actual:
    base_url="http://www.estesparkweather.net/archive_reports.php?date={}".format(actual)
    re= requests.get(base_url)
    soup=bs4.BeautifulSoup(re.text,'lxml')
    table=soup.find_all('table')[0]
    temp=table.find_all('tr',class_='column-light')[0].text.strip()
    hum=table.find_all('tr',class_='column-dark')[0].text.strip()
    temp_new.append(temp)
    hum_new.append(hum)
print(temp,end='\n')
print(hum_new)
   
    
    


# In[138]:


num_days=7
list_format =[today + timedelta(days=i) for i in range(num_days)]
print(list_format)


# In[148]:


num_days=7
list_format=[]
for i in range(num_days):
    list_format1 = today + timedelta(days=i)
    list_format.append(list_format1)
print(list_format)


# In[ ]:


import requests
import bs4
from datetime import timedelta, date, datetime

today = datetime.now()
num_days=100
list_format =[today + timedelta(days=i) for i in range(num_days)]
#print(list_format)
actual =[date.strftime("%d%m%y") for date in list_format]
#print(actual)

for data in actual:
    base_url="http://www.estesparkweather.net/archive_reports.php?date={}".format(actual)
    re= requests.get(base_url)
    soup=bs4.BeautifulSoup(re.text,'lxml')
    table=soup.find_all('table')[0]
    print(table)
    value=[table.find_all('tr')[i].text.strip() for i in range(0,18)] 
    


# In[ ]:


temp=table.find_all('tr',class_='column-light')[0].text.strip()
    hum=table.find_all('tr',class_='column-dark')[0].text.strip()
    temp_new.append(temp)
    hum_new.append(hum)
print(temp_new,end='\n')
print(hum_new)


# ['Jun 1 Average and Extremes', 'Average temperature 44.7°F', 'Average humidity 79%', 'Average dewpoint 37.9°F', 'Average barometer 30.0 in.', 'Average windspeed 2.0 mph', 'Average gustspeed 3.3 mph', 'Average direction 306° ( NW)', 'Rainfall for month 0.27 in.', 'Rainfall for year 6.66 in.', 'Maximum rain per minute 0.03 in. on day 01 at time 13:04', 'Maximum temperature 59.3°F on day 01 at time 10:26', 'Minimum temperature 29.3°F on day 01 at time 05:22', 'Maximum humidity 97% on day 01 at time 07:17', 'Minimum humidity 42% on day 01 at time 10:40', 'Maximum pressure 30.080 in. on day 01 at time 00:35', 'Minimum pressure 29.923 in. on day 01 at time 18:18', 'Maximum windspeed 13.8 mph on day 01 at time 15:08']
# 
# 
# 
# Average temperature (44.7°F), Average humidity (79%),

# In[ ]:





# In[ ]:





# In[11]:


mylist = ['Average temperature (°F)', 'Average humidity (%)',
 'Average dewpoint (°F)', 'Average barometer (in)',
 'Average windspeed (mph)', 'Average gustspeed (mph)',
 'Average direction (°deg)', 'Rainfall for month (in)',
 'Rainfall for year (in)', 'Maximum rain per minute',
 'Maximum temperature (°F)', 'Minimum temperature (°F)',
 'Maximum humidity (%)', 'Minimum humidity (%)', 'Maximum pressure',
 'Minimum pressure', 'Maximum windspeed (mph)',
 'Maximum gust speed (mph)', 'Maximum heat index (°F)']


# In[12]:


mylist


# In[24]:


import requests
import bs4
from datetime import timedelta, date
import datetime

today = datetime.date(2009, 1, 1)
num_days=7
list_format =[today + timedelta(days=i) for i in range(num_days)]
actual =[date.strftime("%d%m%y") for date in list_format]
print(actual)

for data in actual:
    base_url="http://www.estesparkweather.net/archive_reports.php?date={}".format(actual)
    re= requests.get(base_url)
    soup=bs4.BeautifulSoup(re.text,'lxml')
    table=soup.find_all('table')[0]
    #print(table)
    value=[table.find_all('tr')[i].text.strip() for i in range(0,18)] 
    print(value)
    


# In[26]:



Dates_r = pd.date_range(start = ‘01/01/2009’,end = ‘08/05/2020’,freq = ‘M’)
dates = [str(i)[:4] + str(i)[5:7] for i in Dates_r]
dates[0:5]


# In[ ]:





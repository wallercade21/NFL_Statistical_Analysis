#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://www.foxsports.com/nfl/stats?category=passing&season=2023'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[6]:


soup.find('table')


# In[11]:


soup.find_all('table')


# In[59]:


table = soup.find_all('table')


# In[60]:


print(table)


# In[61]:


passing_stats = soup.find_all('th')


# In[63]:


passing_stats


# In[66]:


passing_stats = [title.text.strip() for title in passing_stats]

print(passing_stats)


# In[65]:


passing_stats


# In[24]:


import pandas as pd


# In[144]:


df = pd.DataFrame(columns = passing_stats)

df


# In[147]:


df.insert(0, "RANK", 1)
df


# In[92]:


column_data = soup.find_all('tr')


# In[102]:





# In[148]:


for row in column_data[1: ]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    print(individual_row_data)
    
    length = len(df)
    df.loc[length] = individual_row_data
    


# In[149]:


df


# In[150]:


df.to_csv(r'C:\Users\MattH\OneDrive\Desktop\.csv\PassingLeaders.csv', index = False)


# In[ ]:





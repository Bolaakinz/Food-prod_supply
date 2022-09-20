#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


# In[2]:


ProdDataSet=pd.read_csv(r"https://www.wolframcloud.com/obj/mar/Hamoye/Session%202/Data/Africa%20Food%20Production%20(2004%20-%202013).csv",encoding='latin-1',)
ProdDataSet.head(23110)


# In[5]:


import datetime
today=datetime.datetime(2022, 9, 20)
print(today.strftime("%H:%M:%S %B %d %Y"))


# In[6]:


today.strftime('%m/%d/%Y')


# In[7]:


ProdDataSet.describe()


# In[8]:


ProdDataSet=pd.read_csv(r"https://www.wolframcloud.com/obj/mar/Hamoye/Session%202/Data/Africa%20Food%20Production%20(2004%20-%202013).csv",encoding='latin-1',)
ProdDataSet.groupby('Country')['Value'].agg([np.mean,np.median,max,min,sum])


# In[9]:


ProdDataSet.info()
ProdDataSet.shape


# In[11]:


ProdDataSet.groupby(['Country', 'Year'])['Value'].sum()


# In[22]:


ProdDataSet=pd.read_csv(r"https://www.wolframcloud.com/obj/mar/Hamoye/Session%202/Data/Africa%20Food%20Production%20(2004%20-%202013).csv",encoding='latin-1',)
sns.set_style('dark')
ProdDataSet.groupby('Country')['Value'].sum().sort_values(ascending=False).plot(kind='line',figsize=[10, 5], logy=True)
plt.ylabel('Value(In log Scale)')
plt.xticks(rotation=90)
plt.title('Total Food Production by Country')


# In[13]:


Food_Sup=pd.read_csv(r"https://www.wolframcloud.com/obj/mar/Hamoye/Session%202/Data/Africa%20Food%20Supply%20(2004%20-%202013).csv",encoding='latin-1',)
Food_Sup.head(200)


# In[14]:


Food_Sup.describe()


# In[17]:


data=Food_Sup.groupby('Year')['Value'].sum().sort_values (ascending=False)
fig =plt.figure(figsize=(10,7))
ax = fig.add_axes([0,0,1,1])
bp = ax.boxplot(data)
plt.show


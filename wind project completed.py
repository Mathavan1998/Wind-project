#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('D:/New folder/archive/1. Weather Data.csv')


# In[5]:


data.head(2) #head function is use for top of our data


# In[7]:


data.shape #It shows the Total no of rows & columns of the data frame


# In[8]:


data.index


# In[10]:


data.columns # it show every columns name


# In[12]:


data.dtypes #it shows the types of each columns


# In[17]:


data['Temp_C'].unique() #it show particular columns unique values 


# In[22]:


data.nunique() # it show howmany numbers unique value is there 


# In[23]:


data.count() #it shows how many value is there in each columns


# In[27]:


data['Temp_C'].value_counts() # it shows unique value and how many times it will there


# In[28]:


data.info()


# In[30]:


data.head(2)


# In[31]:


data['Wind Speed_km/h'].unique()


# In[32]:


data['Wind Speed_km/h'].nunique()


# In[33]:


data.head(2)


# In[39]:


data[data['Weather']=='Clear']


# In[38]:


data['Weather'].value_counts()


# In[40]:


data.head(2)


# In[42]:


data[data['Wind Speed_km/h']==4]


# In[45]:


data.isnull().sum()# is show which are the element is missing 


# In[46]:


data.head(2)


# In[54]:


data.rename(columns={'Weather':'Weather condition'},inplace=True) #column name change


# In[53]:


data.head(2)


# In[55]:


data.head(2)


# In[59]:


data['Visibility_km'].describe() # it shows mean std count vales


# In[60]:


data.describe()


# In[61]:


data.var()


# In[63]:


data.head(2)


# In[64]:


data['Weather condition'].value_counts()


# In[66]:


data[data['Weather condition']=='Fog']


# In[71]:


data[data['Weather condition'].str.contains('Fog')].head(20) #it show for with what are there


# In[72]:


data.head(2)


# In[75]:


data[(data['Wind Speed_km/h']>24)&(data['Visibility_km']==25)]


# In[76]:


data.head(2)


# In[82]:


data.groupby('Weather condition').mean()


# In[84]:


data.groupby('Weather condition').min()


# In[85]:


data.groupby('Weather condition').max()


# In[88]:


data[data['Weather condition']=='Fog']


# In[95]:


data[data['Weather condition'].str.contains('Fog')].head(20)


# In[91]:


data.head(2)


# In[97]:


data[(data['Weather condition']=='Clear') | (data['Visibility_km']>40)].head(20)


# In[98]:


data.head(2)


# In[100]:


data[((data['Weather condition']=='Clear')& (data['Rel Hum_%']>50))|(data['Visibility_km']>40)]


# In[ ]:





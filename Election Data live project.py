#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas import Series, DataFrame
import numpy as np


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


from __future__ import division


# In[ ]:


import requests


# In[ ]:


from io import StringIO


# In[ ]:


poll_df=pd.read_csv("indian-state-level-election.csv")
poll_df


# In[ ]:


poll_df.info()


# In[ ]:


poll_df.head()


# In[ ]:


poll_df.tail()


# In[ ]:


poll_df.shape


# In[9]:


sns.factorplot(X='st_name', Y='ac_type',data=poll_df)
plt.show()


# In[10]:


poll_df.head(10)


# In[11]:


sns.factorplot(X='st_name',Y="electors",data=poll_df)
plt.show()


# In[ ]:


sns.catplot(X ='st_name', Y = 'ac_type',data = poll_df,kind = "bar")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





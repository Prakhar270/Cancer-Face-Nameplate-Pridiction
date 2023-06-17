#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


my_list=[[1,2,3],[4,5,6]]


# In[8]:


ar=np.array(my_list)


# In[9]:


print(ar)


# In[10]:


np.arange(0,10)


# In[13]:


np.zeros([5,6],dtype=np.int32)


# In[17]:


ar1=np.linspace(0,10,3)
print(ar1)


# In[18]:


np.eye(4)


# In[19]:


np.empty([5,6])


# In[20]:


np.random.rand(2)


# In[21]:


np.random.randint(1,6,5)


# In[22]:


arr=np.arange(25)
rarr=np.random.randint(0,50,10)


# In[24]:


print(arr)
print(rarr)


# In[30]:


xp=arr.reshape(5,5)
print(xp)


# In[31]:


import pandas as pd


# In[32]:


pd1=pd.DataFrame(xp)
print(pd1)


# In[35]:


labels=['a','b','c']
my_list=[1,2,3]
arl=np.array([10,20,30])
d={'a':10,'b':20,'c':30}


# In[34]:


pd.Series(my_list)


# In[36]:


pd.Series(labels,my_list)


# In[37]:


pd.Series(my_list,labels)


# In[38]:


pd.Series(d)


# In[41]:


a1=pd.Series([1,2,3,4],['USA','GERMANY','USSR','JAPAN'])


# In[42]:


a2=pd.Series([1,2,5,4],['USA','GERMANY','ITALY','JAPAN'])


# In[43]:


a1+a2


# In[51]:


"A B C D".split()


# In[55]:


from numpy.random import randn
np.random.seed(101)


# In[58]:


df=pd.DataFrame(randn(5,4),index="A B C D E".split(),columns="W X Y Z".split())
print(df)


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


5+7


# In[3]:


print(5*3)
print(6+8)


# In[4]:


"integrated development enviroment"


# In[6]:


x=1
id(x)


# In[8]:


x=100


# In[10]:


x=200


# In[11]:


x+7


# In[19]:


python="python is awesome"+"ghh"


# In[15]:


type(python)


# In[16]:


python=100


# In[17]:


type(python)


# In[20]:


python


# In[21]:


int(python)


# In[22]:


ord(python)


# In[25]:


age=input("How old are you")
if age:
    age=int(age)
    if age >= 18 and age<21:
        print("you can enter, but need a wristband!")
    elif age>=21:
        print("you are good to enter and can drink!")
    else:
        print("tou can't come in, little one :(")
else:
    print("Please enter an age")


# In[26]:


user_response=None
while user_response!="please":
    user_response=input("enter")

x=1
# In[31]:


x,*you,y=1,2,2.3,"hello"
print(*you)


# In[32]:


dict1={1:"hello",2:"world",3:"python"}


# In[33]:


dict1[2]


# In[ ]:





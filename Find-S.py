#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import *
import numpy


# In[35]:


data=read_csv("C:\\Users\\exam2\\Downloads\\ENJOYSPORT.csv")


# In[46]:


data


# In[70]:


#Implementing Find-S Algorithm

att=len(data.columns)
h=['@']*(att-1) #Most Specific Hypothesis
print("Most specific hypothesis:",h)
for i in range(len(data)):
    x=list(data.iloc[i,0:att])
    print(f"Instance {i+1} is:")
    print(x[:att-1])
    print()
    if(x[-1]==1):
        for j in range(len(x)-1):
            if h[j]=='@':
                h[j]=x[j]
            elif h[j]!=x[j]:
                h[j]='?'
            else:
                h[j]=x[j]
        print(f"After instance {i+1} the hypothesis is:")
        print(h)
        print()    


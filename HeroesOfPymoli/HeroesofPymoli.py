#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import pandas as pd
import numpy as np


# In[2]:


hero_df = "../Resources/purchase_data.csv"
hero_df = pd.read_csv(hero_df)
hero_df.head(2)


# In[3]:


hero_df.dtypes


# In[90]:


total_players = hero_df["SN"].nunique()
total_playersdf = [{"Total Players": total_players}]
tpdf = pd.DataFrame(total_playersdf)
tpdf


# In[93]:


totals = [{"Number of Unique Items":hero_df["Item ID"].nunique(),
                         "Average Purchase Price":hero_df["Price"].mean(),
                         "Total Number of Purchases":len(hero_df.index),
                         "Total Revenue":hero_df["Price"].sum()}]
totals_df = pd.DataFrame(totals)
totals_df


# In[12]:


cleanhero_df = hero_df.dropna(how = "any")
cleanhero_df.head(2)


# In[15]:


gendergrp = cleanhero_df.groupby(["Gender"])
gendergrp.head(2)


# In[16]:


gender_demographics = pd.DataFrame({"Total Count":gendergrp["Gender"].count(),
                                    "Percentage of players":gendergrp["Gender"].count()/total_players*100})
gender_demographics


# In[60]:


totalgendergrp_df = pd.DataFrame({"Purchase Count":gendergrp["Price"].count(),
                "Average Purchase Price":gendergrp["Price"].mean(),
                "Total Purchase Value":gendergrp["Price"].sum(),
                "Average Purchase Total per Person by Gender":total_purchase_value/gendergrp["Gender"].count()})
totalgendergrp_df


# In[56]:


group_names = ["<10", "10-14", "15-18", "19-22", 
               "23-26", "27-30", "31-34", "35-39",
               "39-40", ">40"]
bins = [0, 9, 13, 17, 21, 25, 29, 33, 37, 40, 100]
agegrp = cleanhero_df.groupby(pd.cut(cleanhero_df["Age"], bins, labels=group_names))
total_age_df = pd.DataFrame({"Purchase Count":age_demo_grp["Price"].count(), 
                            "Average Purchase Price":agegrp["Price"].mean(),
                            "Total Purchase Value":agegrp["Price"].sum(),
                            "Average Purchase Total per Person by Age Group":agegrp["Price"].sum()/agegrp["SN"].nunique()})
total_age_df


# In[58]:


spendgrp = cleanhero_df.groupby(["SN"])
spend_df = pd.DataFrame({"Purchase Count":spendgrp["Price"].count(),
                            "Average Purchase Price":spendgrp["Price"].mean(),
                            "Total Purchase Value":spendgrp["Price"].sum()})
spend_df.head()


# In[59]:


populargrp = cleanhero_df.groupby(['Item ID','Item Name'])
popular_df = pd.DataFrame({"Purchase Count":populargrp ["Price"].count(), 
                            "Item Price":populargrp ["Price"].mean(),
                            "Total Purchase Value":populargrp ["Price"].sum()})
popular_df.head()


# In[102]:


profitgrp = cleanhero_df.groupby(['Item ID','Item Name'])
profit_df = pd.DataFrame({"Purchase Count":profitgrp["Price"].count(), 
                          "Item Price":profitgrp["Price"].mean(),
                          "Total Purchase Value":profitgrp["Price"].sum()})
profit_df.head()


# In[ ]:





# In[ ]:





# In[ ]:


#Three observable remarks from the data set are:
#Ages 23-26 had the highest purchase counts.
#Females paid a higher average purchase count while males had a higher average purchase count.
#The percentage of males is considerably higher than females.


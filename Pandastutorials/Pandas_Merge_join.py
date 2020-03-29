#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])


# In[4]:





# In[21]:


df1.set_index('HPI', inplace=True)


# In[23]:


df3.set_index('HPI', inplace=True)
df3


# In[24]:


joined = df1.join(df3)
joined


# In[25]:


df1 = pd.DataFrame({'Year':[2001,2002,2003,2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   )


df3 = pd.DataFrame({'Year':[2001,2003,2004,2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   )


# In[28]:


display(df3, df1)


# In[41]:


merged = pd.merge(df1, df3, on='Year', how='inner')
merged


# In[42]:


merged.set_index('Year', inplace=True)


# In[43]:


merged


# In[44]:


#Another Example joins


# In[45]:


customers = {
    'CustomerId': [1, 2, 3, 4],
    'CustomerName': ['Anna', 'John', 'Mary', 'Jay'],
    'Country': ['USA', 'Canada', 'Mexico', 'USA']
}
 
orders = {
    'OrderId': [101, 102, 103, 105],
    'CustomerId': [1, 2, 3, 5],
    'OrderDate': ['10/01/2019', '10/02/2019', '10/03/2019', '10/05/2019']
}
 
address = {
    'CustId': [2, 4],
    'Address': ['123 Maple St', '333 Market St']
}


# In[46]:


df_cust = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)
df_address = pd.DataFrame(address)


# In[48]:


display(df_cust, df_orders, df_address)


# In[51]:


df_cust.merge(df_address,how='outer', left_on= 'CustomerId', right_on= 'CustId',)


# In[52]:


df_cust.merge(df_orders, how='left', on='CustomerId')


# In[ ]:





# In[ ]:





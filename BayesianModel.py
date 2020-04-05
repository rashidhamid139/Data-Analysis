#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[15]:


import pandas as pd
import numpy as np

n_draw = 10000
prior_rate  = pd.Series(np.random.uniform(0,1, size = n_draw))


# In[16]:


prior_rate.hist()


# In[17]:


def gen_model(prob):
    return (np.random.binomial(16, prob))


# In[22]:


subscribers = list()
for p in prior_rate:
    subscribers.append(gen_model(p))
observed_data = 6


# In[24]:


post_rate = prior_rate[list(map(lambda x: x == observed_data, subscribers))]
post_rate


# In[25]:


post_rate.hist()


# In[26]:


print('Number of draws left: %d, Posterior mean: %.3f, Posterior median: %.3f, Posterior 95%% quantile interval: %.3f-%.3f' % 
      (len(post_rate), post_rate.mean(), post_rate.median(), post_rate.quantile(.025), post_rate.quantile(.975)))


# In[27]:


sum(post_rate > 0.2)/len(post_rate)


# In[28]:


signups = list()

for p in post_rate:
    signups.append(np.random.binomial(100, p))
    


# In[29]:


signups


# In[31]:


signups = pd.Series([np.random.binomial(n=100,p=p) for p in post_rate])
signups


# In[32]:


signups.hist()


# In[ ]:





# In[ ]:





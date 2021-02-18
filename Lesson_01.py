#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])
mean_a = np.zeros(2)
mean_a = a.mean(axis=0)
print(mean_a)


# In[2]:


a_centered = np.zeros((5, 2))
a_centered[:,:] = mean_a
a_centered = a - a_centered
print(a_centered)


# In[3]:


print(a_centered[:, 0].dot(a_centered[:, 1]) / 4)


# In[4]:


print(np.cov(np.transpose(a),ddof=1))


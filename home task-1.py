#!/usr/bin/env python
# coding: utf-8

# Задание 1.

# In[1]:


import numpy as np


# In[4]:


a = np.array([[1, 6],
            [2, 8],
            [3, 11],
            [3, 10],
            [1, 7]])


# In[11]:


mean_a = a.mean(axis=0)
print ('среднее значение по каждому столбцу', mean_a)


# Задание 2.

# In[23]:


a_centered = a - mean_a
print ('разность', a_centered)


# Задание 3.

# In[36]:


col_1 = a_centered[:, 0]
col_2 = a_centered[:, 1]
col_2_t = col_2.T
a_centered_sp = col_1.dot(col_2_t)
print ('a_centered_sp:', a_centered_sp)


# In[40]:


N = col_1.size
a_centered_sp_n = a_centered_sp / (N - 1)
print ('результат деления:', a_centered_sp_n)


# In[ ]:





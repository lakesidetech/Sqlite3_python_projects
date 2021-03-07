#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sqlite3
#connect to database
#conn=sqlite3.connect('sacco.db')
conn = sqlite3.connect(':memory:')

#create a cursor
c=conn.cursor()

#create a table

c.execute('CREATE TABLE IF NOT EXISTS Users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT,email TEXT)');


c.execute("PRAGMA table_info('Users')")


# In[15]:


c.execute("PRAGMA table_info('Users')").fetchall()


# In[16]:


print(sqlite3.version)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





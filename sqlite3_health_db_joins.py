#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sqlite3, csv

con = sqlite3.connect('health_info.db')
print('db created successcully')


# In[5]:


#create Doctors table
c=con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Doctors(Doctor_id int, Doctor_Name text, Hospital_id int NOT NULL UNIQUE, date_joined text,speciality text, salary int, experience int);")
print('table created successfully')


# In[6]:


#create hospital table
c.execute("CREATE TABLE IF NOT EXISTS Hospital(Hospital_id int NOT NULL UNIQUE,Hospital_name text,Bed_Count int);")
print('table printed successfully')


# In[8]:


import sqlite3, csv

conn=sqlite3.connect('health_info.db')
c=con.cursor()

with open('C:\\Users\\user\\Desktop\\python-files\\doctor_info.csv', 'r') as file:
 for row in file:
   c.execute('INSERT INTO Doctors VALUES(?,?,?,?,?,?,?)', row.split(','))
print('successful insertion')
#join Hospital and Doctors table
c.execute('''SELECT DISTINCT Hospital.Hospital_id, Hospital.Hospital_name, Doctors.Doctor_Name
            FROM Hospital
            LEFT JOIN Doctors ON Hospital.Hospital_id = Doctors.Hospital_id;''')

rows = c.fetchall()
 
for row in rows:
    print(row)
#commmit the health database
con.commit()
    
    


# In[7]:


conn=sqlite3.connect('health_info.db')
c=con.cursor()

with open('C:\\Users\\user\\Desktop\\python-files\\hospital_info.csv', 'r') as file:
 for row in file:
   c.execute('INSERT INTO Hospital VALUES(?,?,?)', row.split(','))
rows = c.fetchall()
 
for row in rows:
    print(row)

con.commit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





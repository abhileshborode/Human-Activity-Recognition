
# coding: utf-8

# In[29]:


from svmutil import *
import os
import numpy as np
import sys
sys.path.append('/home/abhilesh/libsvm/')
import csv


# In[37]:


# It Starts Here
data=np.genfromtxt('hjpd.t',dtype='float')
data.shape


# In[38]:


data=np.genfromtxt('hjpd.t',dtype='float')
ndata=[]
c=np.zeros((1,420))
data.shape
ndatas=[]
ndatass=[]

ad=[]
e=0
b=12
for i in  range(8,56,8):
    for k in range(e,i):
        c=data[k,0:]

        
        for j in range(420):
            #data[i,j]=str(data[i,j])
            #c[i,j]=np.insert((str(j)+ ":" + str(data[i,j])))
            ndata.append(str(j)+ ":" + str(c[j]))



        ndatas.append(ndata) #append elements to rows
        ndata=[] 
    ndatass.append(ndatas)  # append matrix with same label
    ndatas=[]
    e=i
        
        
        


# In[39]:


a1=np.array(ndatass[0])
a2=np.array(ndatass[1])
a3=np.array(ndatass[2])
a4=np.array(ndatass[3])
a5=np.array(ndatass[4])
a6=np.array(ndatass[5])


# In[40]:


add1= 8 * np.ones((8,1),dtype= 'int')
add2= 10 * np.ones((8,1),dtype= 'int')
add3= 12 * np.ones((8,1),dtype= 'int')
add4= 13 * np.ones((8,1),dtype= 'int')
add5= 15 * np.ones((8,1),dtype= 'int')
add6= 16 * np.ones((8,1),dtype= 'int')


cc1=np.column_stack((add1,a1))
cc2=np.column_stack((add2,a2))
cc3=np.column_stack((add3,a3))
cc4=np.column_stack((add4,a4))
cc5=np.column_stack((add5,a5))
cc6=np.column_stack((add6,a6))


# In[41]:


w=np.vstack((cc1,cc2))
w=np.vstack((w,cc3))
w=np.vstack((w,cc4))
w=np.vstack((w,cc5))
w=np.vstack((w,cc6))
print(w.shape)


# In[43]:


np.savetxt('hjpd_d2.t', w, delimiter=" ", fmt="%s") 


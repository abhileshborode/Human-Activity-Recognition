
# coding: utf-8

# In[1]:


from svmutil import *
import os
import numpy as np
import sys
sys.path.append('/home/abhilesh/libsvm/')
import csv


# In[2]:


# It Starts Here


# In[9]:


data=np.genfromtxt('hod_d1.t',dtype='float')
data.shape


# In[10]:


data=np.genfromtxt('hod_d1.t',dtype='float')
ndata=[]
c=np.zeros((1,3360))
data.shape
ndatas=[]
ndatass=[]

ad=[]
e=0
b=12
for i in  range(8,136,8):
    for k in range(e,i):
        c=data[k,0:]

        
        for j in range(3360):
            #data[i,j]=str(data[i,j])
            #c[i,j]=np.insert((str(j)+ ":" + str(data[i,j])))
            ndata.append(str(j)+ ":" + str(c[j]))



        ndatas.append(ndata) #append elements to rows
        ndata=[] 
    ndatass.append(ndatas)  # append matrix with same label
    ndatas=[]
    e=i
        
        
        


# In[11]:


a1=np.array(ndatass[0])
a2=np.array(ndatass[1])
a3=np.array(ndatass[2])
a4=np.array(ndatass[3])
a5=np.array(ndatass[4])
a6=np.array(ndatass[5])
a7=np.array(ndatass[6])
a8=np.array(ndatass[7])
a9=np.array(ndatass[8])
a10=np.array(ndatass[9])
a11=np.array(ndatass[10])
a12=np.array(ndatass[11])
a13=np.array(ndatass[12])
a14=np.array(ndatass[13])
a15=np.array(ndatass[14])
a16=np.array(ndatass[15])




# In[12]:


add1= 1 * np.ones((8,1),dtype= 'int')
add2= 2 * np.ones((8,1),dtype= 'int')
add3= 3 * np.ones((8,1),dtype= 'int')
add4= 4 * np.ones((8,1),dtype= 'int')
add5= 5 * np.ones((8,1),dtype= 'int')
add6= 6 * np.ones((8,1),dtype= 'int')
add7= 7 * np.ones((8,1),dtype= 'int')
add8= 8 * np.ones((8,1),dtype= 'int')
add9= 9 * np.ones((8,1),dtype= 'int')
add10= 10 * np.ones((8,1),dtype= 'int')
add11= 11 * np.ones((8,1),dtype= 'int')
add12= 12 * np.ones((8,1),dtype= 'int')
add13= 13 * np.ones((8,1),dtype= 'int')
add14= 14 * np.ones((8,1),dtype= 'int')
add15= 15 * np.ones((8,1),dtype= 'int')
add16= 16 * np.ones((8,1),dtype= 'int')



cc1=np.column_stack((add1,a1))
cc2=np.column_stack((add2,a2))
cc3=np.column_stack((add3,a3))
cc4=np.column_stack((add4,a4))
cc5=np.column_stack((add5,a5))
cc6=np.column_stack((add6,a6))

cc7=np.column_stack((add7,a7))
cc8=np.column_stack((add8,a8))
cc9=np.column_stack((add9,a9))
cc10=np.column_stack((add10,a10))
cc11=np.column_stack((add11,a11))
cc12=np.column_stack((add12,a12))

cc13=np.column_stack((add13,a13))
cc14=np.column_stack((add14,a14))
cc15=np.column_stack((add15,a15))
cc16=np.column_stack((add16,a16))


# In[13]:


w=np.vstack((cc1,cc2))
w=np.vstack((w,cc3))
w=np.vstack((w,cc4))
w=np.vstack((w,cc5))
w=np.vstack((w,cc6))
w=np.vstack((w,cc7))
w=np.vstack((w,cc8))
w=np.vstack((w,cc9))
w=np.vstack((w,cc10))
w=np.vstack((w,cc11))
w=np.vstack((w,cc12))
w=np.vstack((w,cc13))
w=np.vstack((w,cc14))
w=np.vstack((w,cc15))
w=np.vstack((w,cc16))

print(w.shape)


# In[14]:


np.savetxt('hod_d2.t', w, delimiter=" ", fmt="%s") 


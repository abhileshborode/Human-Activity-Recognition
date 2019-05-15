
# coding: utf-8

# In[1]:


import os
from math import sqrt
import math
import matplotlib.pyplot as plt


# In[2]:


os.getcwd()


# In[3]:


os.listdir(os.getcwd())


# In[4]:


pathTrain=os.path.join(os.getcwd(),'test')


# In[5]:


print(pathTrain)
d=0


# In[6]:


import numpy as np
vectors=np.zeros((48,420))
dd=0
HX=np.zeros((20,7))
HY=np.zeros((20,7))
HZ=np.zeros((20,7))
Rv=np.zeros((1,420))

for filename in sorted(os.listdir(pathTrain)):
    path=os.path.join(pathTrain,filename)
    f=open(path,'r')
    #print (f)
    data = np.genfromtxt(f,dtype = 'float')
    m,n = data.shape
    T1= m/20.0
    T=m/20
    

    dx=np.zeros((20,T))
    dy=np.zeros((20,T))
    dz=np.zeros((20,T))
    
    C=data[0:,2:5]
    
    k=0
    j=20
    d=d+1
    for i in range (T):
        Ins= C[k:j,0:]
           
        dx[:,i] = Ins[0:,0] - Ins[0,1]
        dy[:,i] = Ins[0:,1] - Ins[0,1]
        dz[:,i] = Ins[0:,2] - Ins[0,2]
    
    
    

        k=k+20
        j=j+20


    for l in range(20):
        hx = np.histogram(dx[l,0:],7)
        hy = np.histogram(dy[l,0:],7)
        hz = np.histogram(dz[l,0:],7)

            #normalize
        HX[l,:]=hx[0]/T1
        HY[l,:] =hy[0]/T1
        HZ[l,:] =hz[0]/T1
 
    
    rx=HX.reshape(1,140)
    ry=HY.reshape(1,140)
    rz=HZ.reshape(1,140)
    
    rx=(np.append(rx,ry)).reshape(1,280)
    rx=(np.append(rx,rz)).reshape(1,420)
    
    rx= (np.asarray(rx))
    vectors[dd,:]=rx
    dd=dd+1
    vectors.reshape((48,420))
    
np.savetxt('hjpd_d1.t', vectors, delimiter=' ')


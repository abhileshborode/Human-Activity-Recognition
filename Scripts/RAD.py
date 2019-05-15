
# coding: utf-8

# In[2]:


import os
from math import sqrt
import math


# In[3]:


import os
from math import sqrt
import math


# In[4]:


os.listdir(os.getcwd())


# In[5]:


pathTrain=os.path.join(os.getcwd(),'test')


# In[6]:


print(pathTrain)
d=0


# In[7]:



import numpy as np
dd=0
vectors= np.zeros((48,55))

for filename in sorted(os.listdir(pathTrain)):
    path=os.path.join(pathTrain,filename)
    f=open(path,'r')
    #print (f)
    data = np.genfromtxt(f,dtype = 'float')
    m,n = data.shape
    T1= m/20.0
    T=m/20
    
    n1 = np.zeros((T,5))
    n4 = np.zeros((T,5))
    n8 = np.zeros((T,5))
    n12 = np.zeros((T,5))
    n16 = np.zeros((T,5))
    n20 = np.zeros((T,5))

    C1 = np.zeros((T,3))
    C4 = np.zeros((T,3))
    C8 = np.zeros((T,3))
    C12 = np.zeros((T,3))
    C16 = np.zeros((T,3))
    C20 = np.zeros((T,3))

    d4=np.zeros((T,1),dtype='float')
    d12=np.zeros((T,1),dtype='float')
    d20=np.zeros((T,1),dtype='float')
    d16=np.zeros((T,1),dtype='float')
    d8=np.zeros((T,1),dtype='float')

    angle1=np.zeros((T,1),dtype='float64')
    angle2=np.zeros((T,1),dtype='float64')
    angle3=np.zeros((T,1),dtype='float')
    angle4=np.zeros((T,1),dtype='float')
    angle5=np.zeros((T,1),dtype='float')
    
    
    
    k=0
    j=20
    d=d+1
    for i in range (T):
        Ins= data[k:j,0:]
        n1[i,:] = data[k,0:]
        n4[i,:] = data[k+3,0:]
        n8[i,:] = data[k+7,0:]
        n12[i,:] = data[k+11,0:]
        n16[i,:] = data[k+15,0:]
        n20[i,:] = data[k+19,0:]

        k=k+20
        j=j+20

    C1 = n1[0:,2:5]
    C4 = n4[0:,2:5]
    C8 = n8[0:,2:5]
    C12 = n12[0:,2:5]
    C16 = n16[0:,2:5]
    C20 = n20[0:,2:5]

    for i in range(int(T)):
        d4[i,:] = sqrt( (C1[i,0] - C4[i,0])**2 + (C1[i,1] - C4[i,1])**2 + (C1[i,2] - C4[i,2])**2 )
        d12[i,:] = sqrt( (C1[i,0] - C12[i,0])**2 + (C1[i,1] - C12[i,1])**2 + (C1[i,2] - C12[i,2])**2 )
        d20[i,:] = sqrt( (C1[i,0] - C20[i,0])**2 + (C1[i,1] - C20[i,1])**2 + (C1[i,2] - C20[i,2])**2 )
        d16[i,:] = sqrt( (C1[i,0] - C16[i,0])**2 + (C1[i,1] - C16[i,1])**2 + (C1[i,2] - C16[i,2])**2 )
        d8[i,:] = sqrt( (C1[i,0] - C8[i,0])**2 + (C1[i,1] - C8[i,1])**2 + (C1[i,2] - C8[i,2])**2 )

        # angle 4 and 12
        a1=C4[i,0:]
        b1=C1[i,0:]
        c1=C12[i,0:]
        ba1= a1-b1
        bc1= c1-b1
        cosine_angle1 = np.dot(ba1, bc1) / (np.linalg.norm(ba1) * np.linalg.norm(bc1))
        temp1 = np.arccos(cosine_angle1)
        angle1[i,:]= np.degrees(temp1)


        # angle 12 and 20
        a2=C12[i,0:]
        b2=C1[i,0:]
        c2=C20[i,0:]
        ba2= a2-b2
        bc2= c2-b2
        cosine_angle2 = np.dot(ba2, bc2) / (np.linalg.norm(ba2) * np.linalg.norm(bc2))
        temp2 = np.arccos(cosine_angle2)
        angle2[i,:]= np.degrees(temp2)

        # angle 20 and 16
        a3=C20[i,0:]
        b3=C1[i,0:]
        c3=C16[i,0:]
        ba3= a3-b3
        bc3= c3-b3
        cosine_angle3 = np.dot(ba3, bc3) / (np.linalg.norm(ba3) * np.linalg.norm(bc3))
        temp3 = np.arccos(cosine_angle3)
        angle3[i,:]= np.degrees(temp3)

        # angle 16 and 8
        a4=C16[i,0:]
        b4=C1[i,0:]
        c4=C8[i,0:]
        ba4= a4-b4
        bc4= c4-b4
        cosine_angle4 = np.dot(ba4, bc4) / (np.linalg.norm(ba4) * np.linalg.norm(bc4))
        temp4 = np.arccos(cosine_angle4)
        angle4[i,:]= np.degrees(temp4)


        # angle 8 and 4
        a5=C8[i,0:]
        b5=C1[i,0:]
        c5=C4[i,0:]
        ba5= a5-b5
        bc5= c5-b5
        cosine_angle5 = np.dot(ba5, bc5) / (np.linalg.norm(ba5) * np.linalg.norm(bc5))
        temp5 = np.arccos(cosine_angle5)
        angle5[i,:]= np.degrees(temp5)
    
    tt4 =np.histogram(d4,5)    
    tt12=np.histogram(d12,5)
    tt20=np.histogram(d20,5)
    tt16=np.histogram(d16,5)
    tt8=np.histogram(d8,5)


    aa4 =np.histogram(angle1,6)
    aa12=np.histogram(angle2,6)
    aa20=np.histogram(angle3,6)
    aa16=np.histogram(angle4,6)
    aa8=np.histogram(angle5,6)

    nhd1=(tt4[0].reshape(5,1))
    nhd2=(tt12[0].reshape(5,1))
    nhd3=(tt20[0].reshape(5,1))
    nhd4=(tt16[0].reshape(5,1))
    nhd5=(tt8[0].reshape(5,1))

    nha1=(aa4[0].reshape(6,1))
    nha2=(aa12[0].reshape(6,1))
    nha3=(aa20[0].reshape(6,1))
    nha4=(aa16[0].reshape(6,1))
    nha5=(aa8[0].reshape(6,1))

            #normalize

    nhd1=nhd1/T1
    nhd2=nhd2/T1
    nhd3=nhd3/T1
    nhd4=nhd4/T1
    nhd5=nhd5/T1

    nha1=nha1/T1
    nha2=nha2/T1
    nha3=nha3/T1
    nha4=nha4/T1
    nha5=nha5/T1

    ND = (np.append(nhd1,nhd2)).reshape(10,1)
    ND = (np.append(ND,nhd3)).reshape(15,1)
    ND = (np.append(ND,nhd4)).reshape(20,1)
    ND = (np.append(ND,nhd5)).reshape(25,1)


    NA = (np.append(nha1,nha2)).reshape(12,1)
    NA = (np.append(NA,nha3)).reshape(18,1)
    NA = (np.append(NA,nha4)).reshape(24,1)
    NA = (np.append(NA,nha5)).reshape(30,1)


    vector = (np.append(ND,NA)).reshape(55,1)
    vector= (np.asarray(vector)).T
    vectors[dd,:] = vector
    vectors.reshape((48,55))
    dd=dd+1
        


np.savetxt('rhtfd', vectors, delimiter=' ')


# In[ ]:






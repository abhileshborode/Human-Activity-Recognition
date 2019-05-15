
# coding: utf-8

# In[4]:


import os
from math import sqrt
import math
from numpy import *


# In[5]:


os.listdir(os.getcwd())
pathTrain=os.path.join(os.getcwd(),'test')
print(pathTrain)


# In[6]:



import numpy as np
dd=0
#to train 
#vectors= np.zeros((72,16))
#to test
vectors= np.zeros((48,16))

# iterate through all the files
for filename in sorted(os.listdir(pathTrain)):
    path=os.path.join(pathTrain,filename)
    f=open(path,'r')
    #print (f)
    data = np.genfromtxt(f,dtype = 'float')
    m,n = data.shape
    T1= m/20.0
    T=m/20
    theta=np.zeros((1,T))
    length=np.zeros((1,T))
    bin_num=np.zeros((1,T))

    
    
 
            
    k=0
    j=20

    pt = data[3,2:4]
    for i in range (T):
        Ins=data[k:j,:] 
        CJ=data[k+3,2:4]
        
        ptplus= CJ
        # avoiding divide by zero error
        try:
            
            slope= (ptplus[1]-pt[1])/(ptplus[0]-pt[0])
            
        except Nan:
            
            slope=0
        
        
        thetatemp = math.degrees(math.atan(slope))
        lengthtemp= dist = sqrt( (ptplus[0] - pt[0])**2 + (ptplus[1] - pt[1])**2 )
        bin_numt= (thetatemp*lengthtemp)/360
        
        #calculate length and bin number for each sequence
        length[:,i]= dist = sqrt( (ptplus[0] - pt[0])**2 + (ptplus[1] - pt[1])**2 )
        bin_num[:,i] = (thetatemp*lengthtemp)/360
        
        
        
            
        theta[:,i] = math.degrees(math.atan(slope))

            
            

            

        
        nbin = 8
        
        

        
        pt=ptplus
        
        k=k+20
        j=j+20
        
    #avoiding nan values and replacing them by zero
    where_are_NaNs = isnan(theta)
    theta[where_are_NaNs] = 0    
    
    #find the histogram with 8 equal bins
    th=np.histogram(length,8)
    lh=np.histogram(theta,8)
    
    
    # normalize histogram
    tth=th[0]/T1
    llh=th[0]/T1
    
    #reshape
    tth.reshape(1,8)
    llh.reshape(1,8)
    
    # converting histograms of length and angles into on single line
    hh = (np.append(tth,llh)).reshape(1,16)
    
    
    # mearging histograms of all the data instanses into one single file
    vectors[dd,:] = hh
    dd=dd+1

    
    
    

    
        
            
        
    

#print(vectors.shape)
# save file
np.savetxt('hod_d1ast', vectors, delimiter=' ')


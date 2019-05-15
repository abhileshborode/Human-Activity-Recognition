
# coding: utf-8

# In[1]:


from svmutil import *
import os
import numpy as np
import sys
sys.path.append('/home/abhilesh/libsvm/')
import csv


# In[2]:


# RAD TRY 1
y, x = svm_read_problem('rad_d2.scale')
y1, x1 = svm_read_problem('rad_d2.t.scale')
m = svm_train(y, x, '-t 2 -c 8')
p_label, p_acc, p_val = svm_predict(y1, x1, m)
np.savetxt('pr1.txt',p_label,delimiter=' ')


# In[3]:


# RAD TRY 2
y, x = svm_read_problem('rad_d1.2lib.scale')
y1, x1 = svm_read_problem('rad_d1.t2lib.scale')
m = svm_train(y, x, '-t 2 -c 8')
p_label, p_acc, p_val = svm_predict(y1, x1, m)
np.savetxt('pr2.txt',p_label,delimiter=' ')


# In[4]:


#RAD TRY 3
y, x = svm_read_problem('train.3lib.scale')
y1, x1 = svm_read_problem('test.3lib.scale')
m = svm_train(y, x, '-t 2 -c 256 ')
p_label, p_acc, p_val = svm_predict(y1, x1, m)
np.savetxt('pr3.txt',p_label,delimiter=' ')


# In[6]:


# HJPD TRY 1
y, x = svm_read_problem('hjpd_d2.scale')
y1, x1 = svm_read_problem('hjpd_d2.t.scale')
m = svm_train(y, x, '-t 2 -c 8')
p_label, p_acc, p_val = svm_predict(y1, x1, m)
np.savetxt('phj1.txt',p_label,delimiter=' ')


# In[7]:


# Hjpd TRY 2
y, x = svm_read_problem('hjpd_d22')
y1, x1 = svm_read_problem('hjpd_d2.t2')
m = svm_train(y, x, '-t 2 -c 1024')
p_label, p_acc, p_val = svm_predict(y1, x1, m)
np.savetxt('phj2.txt',p_label,delimiter=' ')


# In[8]:


# HOD TRY 1
y, x = svm_read_problem('hod_d2')
y1, x1 = svm_read_problem('hod_d2.t')
m = svm_train(y, x, '-t 2 -c 1024')
p_label, p_acc, p_val = svm_predict(y1, x1, m)
np.savetxt('ph1.txt',p_label,delimiter=' ')


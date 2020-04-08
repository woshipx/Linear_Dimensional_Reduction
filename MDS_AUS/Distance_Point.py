# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:59:24 2020

@author: xpanz
"""

import numpy as np
import pandas as pd
from sklearn.manifold import MDS
import math
import matplotlib.pyplot as plt

import matplotlib.image as mpimg
#%%
A = np.array([[149.1, 35.3],
             [144.9, 37.8],
             [151.2, 33.9],
             [138.6, 34.9],
             [130.8, 12.3],
             [115.8, 31.7],
             [117.9, 35],
             [118.6,  20.3],
             [153, 27.5],
             [146.88, 19.28],
             [145.8,  16.9],
             [147.3, 42.8]])

D = np.zeros((12,12))
A = (A/180)*math.pi
R = 6371
for i in range (0,12):
    for j in range (0,12):
        C = (math.sin(abs(A[i,1])-(A[j,1])))**2 + math.cos(A[i,1])*math.cos(A[j,1])*(math.sin(abs(A[i,0])-(A[j,0])))**2
        theta = math.asin(math.sqrt(C))
        D[i][j] = theta*R
        
data = D**2
index = ['Canberra','Melbourne','Sydney','Adelade','Darwin','Perth ','Albany','Port Hedland','Brisbane','Townsville ','Cairns','Hobart']
columns = ['Canberra','Melbourne','Sydney','Adelade','Darwin','Perth ','Albany','Port Hedland','Brisbane','Townsville ','Cairns','Hobart']
Word = pd.DataFrame(data,index,columns)
Word
#%%
mds = MDS()
mds.fit(data)
#%%


a = mds.embedding_
print(a)
plt.scatter(a[0:,0],a[0:,1],color='red')
for i,txt in enumerate(index):
    plt.annotate(txt,((a[i,0],a[i,1])))

plt.show()
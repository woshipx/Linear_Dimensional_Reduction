# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:31:28 2020

@author: xpanz
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

index = ['Canberra','Melbourne','Sydney','Adelaide','Darwin','Perth ','Albany','Port Hedland','Brisbane','Townsville ','Cairns','Hobart']
I = Image.open('Map.png')
I = I.rotate(19)
a = np.array([[-11145156.04408105,  -2415867.16513424],
 [ -8602346.45088347,  -4854223.62298165],
 [-12301366.84101709,   -957687.7044222 ],
 [ -3177645.87767724,  -5510068.96559715],
 [ 12145728.24367725,  14665979.43800768],
 [ 19101209.60231381,  -8146056.38208616],
 [ 16595594.06689194,  -10079976.94820382],
 [ 21488712.64687862,   2434404.27626732],
 [-12196451.92518006,   4366215.55072512],
 [ -6603759.76889745,   11622256.93061009],
 [ -3654455.99279432,  13414896.99772139],
 [-12650061.65923095,  -9539872.40490638]])


plt.figure()


a = a/49500
plt.scatter(-1*a[0:,0]+640,-1*a[0:,1]+400,color='red')
for i,txt in enumerate(index):
    plt.annotate(txt,((-1*a[i,0]+650,-1*a[i,1]+400)))
plt.imshow(I)

plt.show()

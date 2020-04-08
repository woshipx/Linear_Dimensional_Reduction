# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:06:06 2020

@author: xpanz
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image

index = ['Canberra','Melbourne','Sydney','Adelade','Darwin','Perth ','Albany','Port Hedland','Brisbane','Townsville ','Cairns','Hobart']
# input matrix , the first colume is longitude and the second colume is latitude
A = np.array([[149.1, 35.3],    
             [144.9, 37.8],
             [151.2, 33.9],
             [138.6, 34.9],
             [130.8, 12.3],
             [115.8, 31.7],
             [121.9, 33.84],
             [118.6,  20.3],
             [153, 27.5],
             [146.88, 19.28],
             [145.8,  16.9],
             [147.3, 42.8]])
def Cal_dis(A):
    '''this function transform the latitude and longitude into distance'''    
    D = np.zeros((12,12))
    A = (A/180)*math.pi  #degree to radian
    R = 6371    #average radium of earth
    for i in range (0,12):
        for j in range (0,12):  #Haversine algorithm to calculate the distance between two point in sphere
            C = (math.sin(abs(A[i,1])-(A[j,1])))**2 + math.cos(A[i,1])*math.cos(A[j,1])*(math.sin(abs(A[i,0])-(A[j,0])))**2
            theta = math.asin(math.sqrt(C))
            D[i][j] = theta*R  
    return D




def classical_MDS(D):

    D = Cal_dis(A)**2   #calculate matrix D^2
    (n1, n2) = D.shape  #get the size of D
    H = np.eye(n1) - np.ones(n1)/n1   # create H matrix using double centring
    B = (-1/2)*H*D*H


    eig_val, eig_vector = np.linalg.eig(B)  #calculate the eigenvalue and eigenvector of B
    index_eig_val = np.argsort(-eig_val)[:2]    # the index reverse list of eigenvalue
    eig_val = eig_val[index_eig_val]    # form the eigenvalue from largest to small
    eig_vec = eig_vector[:, index_eig_val]  # form the eigenvalue from largest to small
    X = eig_vec*np.sqrt(eig_val)    #calculate the matrix X 
    return X



def reshape_image(a,I):

    I = I.rotate(19)    #rotete image 18 degrees

    plt.figure()    #plot city location in the map
    a = a*2.1   #reshape points coordinates
    plt.scatter(a[0:,0]+600,-1*a[0:,1]+370,color='red') #plot points
    for i,txt in enumerate(index):  #plot name of each city
        plt.annotate(txt,((a[i,0]+600,-1*a[i,1]+370)))
#        plt.imshow(I)   #plot image

    plt.show()  

D = Cal_dis(A)
a = classical_MDS(D)
I = Image.open('Map.png')
reshape_image(a,I)